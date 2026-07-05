import sys
from ft_filter import ft_filter

def main() :
    try:
        if len(sys.argv) != 3:
            raise AssertionError ("the arguments are bad")
        
        texte = sys.argv[1]

        #The second argument should be an int
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        #Do separation of text in words
        words = texte.split()

        #create lamdba funciton and apli ft_filter
        result = ft_filter(lambda word: len(word) > n, words)

        print(list(result)) #format the result in a list
        
    except AssertionError as msg: 
        print(f"AssertionError: {msg}")
        


if __name__ == "__main__" :
    main()