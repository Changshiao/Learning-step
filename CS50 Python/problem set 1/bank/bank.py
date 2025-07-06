greet = str(input("Greeting: ")).lower().split()

if 'hello' in greet:
    print("$0")
elif greet[0].startswith("h") :
    print("$20")
else:
    print("$100")
