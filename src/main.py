import sys, os
from token import Token
from analisador_lexico import analisador_lexico

def main():
    filename = sys.argv[1]
    if filename and os.path.exists(filename):
        analisador_lexico().read_whole_file(filename)
    else:
        print("File does not exist.")
            
if __name__ == '__main__':
    main()