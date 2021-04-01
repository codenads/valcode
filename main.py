import sys
import os
from token import Token
from lexical_analyzer import lexical_analyzer


def main():
    filename = sys.argv[1]
    if filename and os.path.exists(filename):
        lexical_analyzer().parse_file(filename)
    else:
        print("Unable to find file or path.")


if __name__ == '__main__':
    main()
