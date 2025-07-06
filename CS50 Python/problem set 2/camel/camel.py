msg=input("camelCase: ")
snake_case=""
for letter in msg:
    if letter.isupper():
        snake_case+="_"+letter.lower()
    else:
        snake_case+=letter
print("snake_case:",snake_case)

