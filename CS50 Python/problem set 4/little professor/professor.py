import random


def wrong_function(num1, num2):
    for i in range(2):
        try:
            answer = int(
                input(
                    f"{num1} + {num2} = ",
                )
            )
            if answer == num1 + num2:
                return True
            else:
                print("EEE")
                pass
        except ValueError:
            print("EEE")
            pass
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")


def main():
    level = get_level()
    right = 0
    for i in range(10):
        num1, num2 = generate_integer(level)
        sum = num1 + num2
        print(f"{num1} + {num2} = ", end="")
        try:
            answer = int(input(""))
            if answer == sum:
                right = right + 1
                pass
            else:
                print("EEE")
                wrong_function(num1, num2)
        except ValueError:
            print("EEE")
            wrong_function(num1, num2)
    print(f"Score: {right}")


def get_level():
    while True:
        try:
            level = input("Level: ")
        except ValueError:
            pass
        else:
            if level in ["1", "2", "3"]:
                return int(level)
            else:
                pass


def generate_integer(level):
    if level == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    elif level == 3:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)
    return num1, num2


if __name__ == "__main__":
    main()
