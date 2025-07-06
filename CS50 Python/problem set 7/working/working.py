import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r"^([1-9]|1[0-2]):([0-5][0-9]) AM to ([1-9]|1[0-2]):([0-5][0-9]) PM$",s.strip()):
        match_obj=re.search(r"^([1-9]|1[0-2]):([0-5][0-9]) AM to ([1-9]|1[0-2]):([0-5][0-9]) PM$",s.strip())
        start_hour = int(match_obj.group(1))
        start_minute = int(match_obj.group(2))
        end_hour = int(match_obj.group(3))+12
        end_minute = int(match_obj.group(4))
        return (f'{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}')

    else:
        raise ValueError

if __name__ == "__main__":
    main()
