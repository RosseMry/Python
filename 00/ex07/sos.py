import sys

def main():
    NESTED_MORSE = {
    " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", 
    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", 
    "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", 
    "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", 
    "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", 
    "Y": "-.-- ", "Z": "--.. ", "0": "----- ", "1": ".---- ", 
    "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ", 
    "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. " }

    try : 
        if len(sys.argv) != 2 :
            raise AssertionError ("the arguments are bad")

        txt = sys.argv[1]

        for character in txt:
            if not character.isalnum() and character != " ":
                raise AssertionError ("the arguments are bad")

        txt_upper = txt.upper()

        morse_code = [NESTED_MORSE[character] for character in txt_upper]

        result = "".join(morse_code).strip()
        print(result)
    except AssertionError as msg:
        print(f"AssertionError: {msg}")

if __name__ == "__main__":
    main()