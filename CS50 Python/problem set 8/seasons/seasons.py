from datetime import date
import re
import sys
import inflect

def get_time(input_date):
    if re.match(r'^(([1-9])|(1\d{1,3})|(200\d|201\d)|(202[0-4]))-((0[0-9]|1[0-2]))-([0-2]\d|(3[0-1]))$', input_date.strip()):
        year, month, day = input_date.strip().split('-')
        return year, month, day
    else:
        return False

def main():
    birth = input("Date of Birth: ")
    try:
        if re.match(r'^(([1-9])|(1\d{1,3})|(200\d|201\d)|(202[0-4]))-((0[0-9]|1[0-2]))-([0-2]\d|(3[0-1]))$', birth.strip()):
            time = get_time(birth)
        else:
            sys.exit('Invalid date')
    except:
        sys.exit('Invalid date')
    birth_date = date(int(time[0]), int(time[1]), int(time[2]))
    today = date.today()
    diff = (today - birth_date).days
    diff_minute = diff * 24 * 60
    p = inflect.engine()
    words = p.number_to_words(diff_minute, andword='')
    print(words.capitalize() + ' minutes')

if __name__ == "__main__":
    main()
