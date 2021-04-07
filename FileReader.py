BYTE = 1


class FileReader:
    def __init__(self, file):
        self.file = open(file, 'r')

        self.line = 0
        self.column = 1
        self.spaces = 0

        self.file_line = ""
        self.words = []

    def split(self, line):
        words = []
        flag = False

        word = ""
        for char in line:
            if char == "\n":
                if word:
                    words.append({'lexeme': word, 'spaces': self.spaces})
                    word = ""
                break
            elif char == " ":
                if word and not flag:
                    words.append({'lexeme': word, 'spaces': self.spaces})
                    word = ""
                self.spaces += 1
            elif char == "\"" or char == "\'":
                if flag:
                    word = f'{char}{word}{char}'
                if word:
                    words.append({'lexeme': word, 'spaces': self.spaces})
                    word = ""
                flag = not flag
            else:
                word += char

        if word:
            words.append({'lexeme': word, 'spaces': self.spaces})

        if words and words[0]['lexeme'][0] == "#":
            return None
        else:
            return words

    def next_word(self):
        while not self.words:
            self.file_line = self.file.readline()

            if not self.file_line:
                return None

            self.words = self.split(self.file_line)

            self.line += 1
            self.column = 1
            self.spaces = 0

            end = ""

            if self.file_line[-1] != "\n":
                end = "\n"

            print(f'{str(self.line).rjust(4)}  {self.file_line}',
                  end=end)

        return self.words.pop(0)
