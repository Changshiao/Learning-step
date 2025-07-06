import pyautogui
import time
from PIL import Image

redpoint_path=r'images\redpiont.png'

wechat_path=r'images\new_wechat.png'

message_input_box=r'images\sent.png'


def resize(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    target_size = (120, 100)
    resized_image = image.resize(target_size)
    resized_image.save(image_path)
    #调整图片尺寸以及格式修改

def locate_and_double_click(image_path):
    # 定位并点击指定图片
    location = pyautogui.locateCenterOnScreen(image_path,confidence=0.6)
    if location is not None:
        pyautogui.doubleClick(location[0], location[1])
        return True
    else:
        return False

def locate_and_click(image_path):
    # 定位并点击/指定图片
    location = pyautogui.locateCenterOnScreen(image_path,confidence=0.8)
    print('located')
    if location is not None:
        pyautogui.click(location[0], location[1])
        return True
    else:
        return False

def send_auto_reply(message):
    # 点击微信图标（假设微信图标已经在屏幕上）
    resize(wechat_path)
    if locate_and_double_click(wechat_path):
        time.sleep(2)  # 等待微信启动
        # 定位消息输入框并点击
        print("Done1")
        try:
            locate_and_click(redpoint_path)
            print("Done2")
        except:
            print("No one send msg")
        else:
            # 输入自动回复消息
            pyautogui.write(message)
            pyautogui.press('enter')
            locate_and_click(message_input_box)
                  # 发送消息
            print("Done3")
    else:
        print("Can't Find Wechat.png")


def main():
    auto_reply_message ='Sorry,busy now,Talk to you later.'
    while 1:
        send_auto_reply(auto_reply_message)


if __name__ == "__main__":
    main()
