import random
import sys
while True:
    try:
        level=int(input("level: "))
    except ValueError:
        pass
    else:
        if level < 1:
            pass
        else:
            break

gsint = random.randint(1, level)


while True:
    try:
        msg = int(input("Guess:"))
    except ValueError:
        pass
    else:
        if msg > gsint:
            print("Too large!")
        elif msg < gsint:
            print("Too small!")
        else:
            print("Just right!")
            sys.exit(1)
