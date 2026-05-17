import sys

def count_characters(text):
    print("The text contains" + len(text) + " characters:")
    print("")


def main():
    if len(sys.argv) > 2 :
        print("AssertionError: more than one argument is provided")
        exit();
    else :
        text = input("What is the text to count?")
        count_characters(text)


if __name__ == "__main__":
    main()