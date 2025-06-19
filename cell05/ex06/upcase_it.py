import sys

try:
    print(sys.argv[1].upper())
except IndexError :
    print("none")
