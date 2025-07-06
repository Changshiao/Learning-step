import sys
import os.path
from PIL import Image, ImageOps

def main():
    check_format()
    get_clothed()

def check_format():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if check_file_format(sys.argv[1])==False:
        sys.exit("Invalid input")
    if check_file_format(sys.argv[2])==False:
        sys.exit("Invalid output")
    format1 = os.path.splitext(sys.argv[1])
    format2 = os.path.splitext(sys.argv[2])
    if format1[1]!=format2[1]:
        sys.exit("Input and output have different extensions")

def check_file_format(filename):
    file=os.path.splitext(filename)
    if file[1] in ['.jpg','.jpeg','.png']:
        return True
    else:
        return False

def get_clothed():
    try:
            muppetfile=Image.open (sys.argv[1])
            shirt=Image.open("shirt.png")
            size=shirt.size
            muppet=ImageOps.fit(muppetfile,size)
            muppet.paste(shirt,shirt)
            muppet.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__=="__main__":
    main()
