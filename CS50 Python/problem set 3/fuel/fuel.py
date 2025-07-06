def Function():
    while True:
        try:
            msg=input("Fraction: ")
            nm,dm=msg.split("/")
            num=int(nm)/int(dm)
        except(ValueError,ZeroDivisionError):
            pass
        else:
            if num>=0.9 and num<=1:
                return 'F'
            elif num<=0.1:
                return 'E'
            elif num>1:
                pass
            else:
                return num

def main():
    num=Function()
    if isinstance(num, str) and num.isalpha():
        print(num)
    else:
        rounded_num = round(num * 100)
        print(f"{rounded_num}%")
main()

