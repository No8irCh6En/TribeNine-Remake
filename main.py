from start_menu import is_start_menu, click_start_setup, click_delete_accout, click_start_game

from in_game import is_in_game, get_mail_reward, get_fes_reard, satis_or_not, gacha

# 配置参数
TARGET_DIR = "images/targets/"
IMG_DIR = "images/"
STAR_IMAGE_NAME = "star.png"  # 假设star图片命名为star.png
CHECK_INTERVAL = 5  # 每5秒检查一次
MAX_STAR_COUNT = 2  # star图片出现两次时停止


# def main():
#     # 获取目标图片列表
#     object_images = [os.path.join(IMG_DIR, img) for img in os.listdir(IMG_DIR)]
#     target_images = [os.path.join(TARGET_DIR, img) for img in os.listdir(TARGET_DIR)]
#     star_count = 0  # star图片出现次数
#     current_index = 0  # 当前比对的图片索引

#     while True:
#         # 截取屏幕
#         screen = capture_screen()

#         # 检查当前图片是否匹配
#         ## TODO
#         current_image = object_images[current_index]
#         if match_template(screen, current_image):
#             print(f"匹配成功：{current_image}")
#             if STAR_IMAGE_NAME in current_image:
#                 star_count += 1
#                 if star_count >= MAX_STAR_COUNT:
#                     print("检测到star图片出现两次，停止操作。")
#                     break
#             current_index += 1  # 移动到下一张图片
#             if current_index >= len(target_images):
#                 current_index = 0  # 如果所有图片都比对完，重新开始
#         else:
#             print(f"未匹配到：{current_image}")

#         # 等待一段时间后继续
#         time.sleep(CHECK_INTERVAL)

def main():
    return

if __name__ == "__main__":
    main()