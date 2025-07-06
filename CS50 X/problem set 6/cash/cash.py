count = 0
while True:
    try:
        cash = float(input("Change:")) * 100
    except ValueError:
        continue
    else:
        if cash > 0:
            while cash > 0:
                if cash >= 25:
                    cash -= 25
                    count += 1
                elif cash >= 10:
                    cash -= 10
                    count += 1
                elif cash >= 5:
                    cash -= 5
                    count += 1
                elif cash >= 1:
                    cash -= 1
                    count += 1

            print(count)
            break
        else:
            print("Invalid input. Please enter a positive change amount.")
