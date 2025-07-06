import sys
from validator_collection import validators, checkers, errors


def main():
    try:
        email_address = validators.email(input("What's your email address?"))
    except errors.EmptyValueError:
        print('Invalid')
    except errors.InvalidEmailError:
        print('Invalid')
    else:
        print("valid")
if __name__ == "__main__":
    main()
