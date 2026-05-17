import sys


if len(sys.argv) == 1 :
    exit()
elif(len(sys.argv) > 2) :
    print("AssertionError: more than one argument is provided")
    exit()
try :
    n = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    exit()
if int(sys.argv[1]) % 2 == 0 :
    print("I'm Even.")
    exit()
elif int(sys.argv[1]) % 2 != 0 :
    print("I'm Odd.")
    exit()
