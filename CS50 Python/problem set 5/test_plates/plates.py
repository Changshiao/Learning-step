def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    else:
        if s.isalpha():
            return True
        for letters in s:
            if letters.isdigit():
                position=s.index(letters)
                if s[position:].isdigit() and s[position]!='0':
                    return True
                else:
                    return  False
        return False

if __name__=="__main__":
    main()
