def main():
    message = input("Input: ")
    msg_wo_vowels = shorten(message)
    print("Output: " + msg_wo_vowels)


def shorten(word):
    wo_vowels = ""
    for letter in word:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            wo_vowels += letter
    return wo_vowels



if __name__ == "__main__":
    main()
