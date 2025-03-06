import cv2
import os
import numpy as np
import pyautogui

def match_template(screen, template_path, threshold=0.8):
    """
    使用模板匹配检测目标图片是否出现在屏幕上。
    :param screen: 屏幕截图（numpy数组）。
    :param template_path: 目标图片路径。
    :param threshold: 匹配阈值，默认为0.8。
    :return: 是否匹配成功（bool）以及匹配位置（x, y, w, h）。
    """
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        w, h = template.shape[::-1]  # 获取模板的宽度和高度
        return True, (max_loc[0], max_loc[1], w, h)  # 返回匹配成功和位置信息
    else:
        return False, None

def matchAndClick(template_path, threshold=0.8, click_offset=(0, 0)):
    """
    在屏幕上查找目标图片，并点击匹配位置。
    :param template_path: 目标图片路径。
    :param threshold: 匹配阈值。
    :param click_offset: 点击偏移量（相对于匹配位置的中心）。
    :return: 是否匹配成功并点击。
    """
    # 捕获屏幕
    screen = np.array(pyautogui.screenshot())
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    # 检测目标图片
    is_match, match_info = match_template(screen, template_path, threshold)

    if is_match:
        x, y, w, h = match_info
        click_x = x + w // 2 + click_offset[0]  # 计算点击位置（中心点 + 偏移量）
        click_y = y + h // 2 + click_offset[1]

        # 模拟鼠标点击
        pyautogui.click(click_x, click_y)
        return True
    else:
        return False
    
def matchAndFlip(template_path, threshold=0.8, flip_distance=200):
    """
    在屏幕上查找目标图片，一旦匹配成功就执行下滑操作。
    :param template_path: 目标图片路径。
    :param threshold: 匹配阈值。
    :param flip_distance: 下滑的距离（像素）。
    :return: 是否匹配成功并执行了下滑操作。
    """
    # 捕获屏幕
    screen = np.array(pyautogui.screenshot())
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    # 检测目标图片
    is_match, match_info = match_template(screen, template_path, threshold)

    if is_match:
        # 先移动到特定点，再执行下滑操作
        pyautogui.moveTo(match_info[0],match_info[1])
        pyautogui.scroll(-flip_distance)  # 向下滑动
        return True
    else:
        return False

