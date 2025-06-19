import sys

try:
    print(sys.argv[1].lower())
except IndexError :
    print("none")
