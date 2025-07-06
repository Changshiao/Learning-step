def main():
    i = input("What time is it? " )
    x = convert(i)

    if i == "12:00 p.m.":
        print("lunch time")
    elif 7 <= float(x) <= 8:
        print("breakfast time")
    elif 12 <= float(x) <= 13:
        print("lunch time")
    elif 18 <= float(x) <= 19:
        print("dinner time")

def convert(time):
    if time.endswith("p.m."):
        h, y, = time.split(":")
        m = y.strip("p.m.").strip("a.m.")
        t= float(h) + float(m)/60 + 12
        return t

    else:
        h, y, = time.split(":")
        m = y.strip("p.m.").strip("a.m.")
        t= float(h) + float(m)/60
        return t

if __name__ == "__main__":
    main()
