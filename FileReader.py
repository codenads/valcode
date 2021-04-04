class FileReader:
    def __init__(self, file):
        self.file = open(file, 'r')
        self.line = 1
        self.column = 1
        self.str_flag = False

    def str_find(self):
        str_acc = '"'
        while True:
            char = self.file.read(1)
            str_acc += char
            if char == '"':
                self.str_flag = False
                return str_acc

    def read(self):
        word = ""
        while True:
            if self.str_flag:
                word = self.str_find()
                break
            else:
                char = self.file.read(1)

                if not char:
                    return None

                self.column += 1

                if char == '"':
                    self.str_flag = True
                    break
                elif char == ' ':
                    if word:
                        break
                elif char == '\n':
                    self.line += 1
                    self.column = 1
                    if word:
                        break
                else:
                    word += char

        return word
