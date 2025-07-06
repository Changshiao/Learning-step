from project import locate_and_click
from project import resize
from PIL import Image

file_path='Images/test_image.png'
new_file_path='Images/test_image2.png'
mag_path='magnifying glass.png'

def test_locate_and_click():
    assert locate_and_click(file_path)==False

def test_resize():
    resize(new_file_path)
    image=Image.open(new_file_path)
    assert image.size==(120, 100)

def test_locate_and_click2():
    assert locate_and_click(mag_path)==True


def main():
    test_locate_and_click()
    test_locate_and_click2()
    test_resize()

if __name__ == "__main__":
    main()
