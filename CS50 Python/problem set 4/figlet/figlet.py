import sys
import random

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    try:
        figlet.setFont(font=sys.argv[2])
    except Exception as e:
        print("Invalid usage:", str(e))
        sys.exit(1)

else:
    print("Invalid usage")
    sys.exit(1)


msg = input("Input:")
print("Output: ")
print(figlet.renderText(msg))
