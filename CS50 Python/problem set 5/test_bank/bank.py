def value(greet):
    new_greet=greet.lower().strip()
    if 'hello' in new_greet:
        return 0
    elif new_greet[0].startswith("h") :
        return 20
    else:
        return 100

def main():
    greet = input("Greeting: ")
    money=value(greet)
    print(f"${money}")


if __name__ == "__main__":
    main()
