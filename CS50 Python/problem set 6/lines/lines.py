import sys
count=0
def main():
    global count
    check_py_file()
    count_line()
    print(count)



#1.check python file
#2.check line
def check_py_file():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too much command-line arguments")
    else:
        if sys.argv[1].endswith(".py")==False:
            sys.exit("Not a Python file")

def count_line():
    global count
    try:
        with open(f"{sys.argv[1]}","r") as File:
            for line in File.readlines():
                if check_line(line)==True:
                    count+=1

    except FileNotFoundError:
        sys.exit("File does not exist")

def check_line(line):
    if line.isspace()==True:
        return False
    elif line.strip().startswith("#")==True:
        return False
    else:
        return True

if __name__=="__main__":
    main()
