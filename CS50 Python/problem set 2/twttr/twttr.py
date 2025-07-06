msg=input("set up your twtter:")

for letter in msg:
    if letter in ['a','e','i','o','u','A','E','I','O','U']:
        print("",end="")
    else:
        print(letter,end="")

print("")
