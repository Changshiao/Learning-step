# AutoResponser
#### Video Demo:  <[URL HERE](https://www.youtube.com/watch?v=dJ-SYXPO8tA)>
#### Description：Todays,Wechat is an irreplaceable software in our daily life.But sometimes,we are too busy to response the msg at once.Therefore,I write a little project to solve this knotty problem.

### I got these different ideas to solve the problem:

1.Just use the package written by other programmers like ItChat,but...it seems a little dangerous to use it.OK,just pass it.

2.Using the API offered by Wechat.Then I can call the API,but I have to get WeChat developer permissions,It's too troublesome

3.It's the easiest way to solve the problem.All that I need to mock my mouse and my keyboard,Just click click and click!

### How To Do It?

It seems that I need some packages.Like the OpenCV,image,pyautogui,Pillow,time.I hope these powerful packages can help me to finish my project.

I need nonitor my desktops(pyautogui is necessary),if someone send msg ,a redpoint would shown up on the desktops.The next step is searching the redpoint and click it (the function called locateCenter is needed).The last step is input the msg I prepared and click the message_input_box.

### Preparation:

import pyautogui
import time(Make all the program more fluency)
from PIL import Image(Modify the image to enhance the image search efficiency)
preparing the images in "images file"(locateCenter need the images to search the target image)

### Implementation process:

```python
    resize(image_path):
        image = Image.open(image_path)
        image = image.convert("RGB")
        target_size = (120, 100)
        resized_image = image.resize(target_size)
        resized_image.save(image_path, "png")
```
 I can use this function to resize my picture to prevent the search of pictures from being affected by resolution and size problems

 ```python
    locate_and_double_click(image_path):
        location = pyautogui.locateCenterOnScreen(image_path,confidence=0.6)
        if location is not None:
            pyautogui.doubleClick(location[0], location[1])
            return True
        else:
            return False
 ```
 It's easy to understand that this functon is to locate and click on the specified image.I use 0.6 as the threshold so that the likelihood of finding the specified image will be higher.

 ```python
    send_auto_reply(message):
        resize(wechat_path)
        if locate_and_double_click(wechat_path):
            time.sleep(2)
            print("Done1")
            try:
                locate_and_click(redpoint_path)
                print("Done2")
            except:
                print("No one send msg")
            else:
                pyautogui.write(message)
                pyautogui.press('enter')
                locate_and_click(message_input_box)
                print("Done3")
        else:
            print("Can't Find Wechat.png")
 ```
 This function is to find Wechat and open it,similar to the previous instruction.

```python
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
        resized_image.save(image_path, "png")

    def locate_and_double_click(image_path):
        location = pyautogui.locateCenterOnScreen(image_path,confidence=0.6)
        if location is not None:
            pyautogui.doubleClick(location[0], location[1])
            return True
        else:
            return False

    def locate_and_click(image_path):
        location = pyautogui.locateCenterOnScreen(image_path,confidence=0.8)
        print('located')
        if location is not None:
            pyautogui.click(location[0], location[1])
            return True
        else:
            return False

    def send_auto_reply(message):
        resize(wechat_path)
        if locate_and_double_click(wechat_path):
            time.sleep(2)
            print("Done1")
            try:
                locate_and_click(redpoint_path)
                print("Done2")
            except:
                print("No one send msg")
            else:
                pyautogui.write(message)
                pyautogui.press('enter')
                locate_and_click(message_input_box)
                print("Done3")
        else:
            print("Can't Find Wechat.png")


    def main():
        auto_reply_message ='Sorry,busy now,Talk to you later.'
        while 1:
            send_auto_reply(auto_reply_message)


    if __name__ == "__main__":
        main()
```
It is the all project.

This is CS50P,I'm Shiao.I'm very happy to finish my course with this project.I'll take CS50x later.

Thank you David J. Malan,thank you CS50.
