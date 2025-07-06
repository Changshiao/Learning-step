
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
dmon = {}
j = 1
for i in months:
    dmon[i] = j
    j += 1

def main():
    while True:
        date = input("Date: ")
        if "/" in date:
            try:
                m, d, y = date.split("/")
                if int(m) < 1 or int(m) > 12 or int(d) < 1 or int(d) > 31:
                    pass
                else:
                    print(f"{int(y):04d}-{int(m):02d}-{int(d):02d}")
                    break
            except:
                pass
        elif "," in date:
            try:
                m, d, y = date.split(" ")
                d = d.removesuffix(",")
                if int(d) < 0 or int(d) > 31:
                    pass
                elif m not in months:
                    pass
                else:
                    print(f"{int(y):04d}-{dmon[m]:02d}-{int(d):02d}")
                    break
            except:
                pass
main()
