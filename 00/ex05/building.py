import sys
import string

def count_characters(text):
    print(f"The text contains {len(text)} characters:")
    upper = 0
    lower = 0
    spaces = 0
    digits = 0
    punct = 0
    for char in text :
        if char.isupper() :
            upper += 1
        elif char.islower() :
            lower += 1
        elif char.isdigit() :
            digits += 1
        elif char.isspace() :
            spaces += 1
        elif char in string.punctuation : #dont have function for puntuations, forced to add string librerie
            punct += 1
    
    print( f"{upper} upper letters \n{lower} lower letters \n{punct} punctuation marks\n{spaces} spaces \n{digits} digits" )
        


def main():
    if len(sys.argv) > 2 : #len bcs dont work argc
        print("AssertionError: more than one argument is provided")
        sys.exit()
    elif len(sys.argv) == 2:
        count_characters(sys.argv[1])
    else :
        text = input("What is the text to count?\n")
        count_characters(text)


if __name__ == "__main__":
    main()