menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
total_amount = 0
while True:
    try:
        food = input("What's the food? ").title()
        if food not in menu:
            pass
        else:
            total_amount += menu[food]
            print("${:.2f}".format(total_amount))

    except EOFError:
        break
