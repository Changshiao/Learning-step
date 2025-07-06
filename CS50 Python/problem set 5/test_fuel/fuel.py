def main():
    msg=input()
    print(gauge(convert(msg)))


def convert(fraction):

    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    percentage = x/y*100

    if percentage >= 0 and percentage <= 100:
        return round(percentage)

    else:
        return ValueError


def gauge(percentage):

    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
