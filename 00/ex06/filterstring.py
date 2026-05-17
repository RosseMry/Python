import sys
from ft_filter import ft_filter

def main() :
    if len(sys.argv) > 3 :
        print("AssertionError: more than one argument is provided")
        sys.exit()
    elif len(sys.argv) < 3:
        print("AssertionError: the arguments are bad")
        sys.exit()
    else
        ft_filter(sys.argv[1], sys.argv[2])


if __name__ == "__main__" :
    main()