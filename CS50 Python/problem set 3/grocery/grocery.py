grocery = {}

while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        break
sorted_items = sorted(grocery.items(), key=lambda x: x[0])
for item in sorted_items:
    print(item[1], item[0])
