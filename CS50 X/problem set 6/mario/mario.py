from cs50 import get_int
while True:
    hight=get_int(("Hight:"))
    if (hight<1 or hight>8):
        continue
    for line in range(1,hight+1):
        print(" "*(hight-line),end='')
        print("#"*line,end='')
        print()
    break
