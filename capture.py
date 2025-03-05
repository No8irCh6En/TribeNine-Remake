import pyautogui
import cv2
import numpy as np

def capture_screen(region=None):
    """
    截取屏幕图像。
    :param region: 可选参数，指定截取的屏幕区域 (x, y, width, height)。
    :return: 截取的屏幕图像（numpy数组）。
    """
    screenshot = pyautogui.screenshot(region=region)
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame