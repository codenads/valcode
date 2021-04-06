import sys
import os
from LexicalAnalyzer import LexicalAnalyzer


def main():
    filename = sys.argv[1]
    if filename and os.path.exists(filename):
        lexical_analyzer = LexicalAnalyzer(filename)
        while True:
            token = lexical_analyzer.next_token()
            if not token:
                break
            token.show()
    else:
        print("Unable to find file or path.")


if __name__ == '__main__':
    main()
