BYTE = 1


class FileReader:
    def __init__(self, file):
        self.file = open(file, 'r')
        self.line = ""
        self.word_list = []
        # self.line = 1
        # self.column = 1
        # self.accumulator = ""

    def split(line):
        word_list = []
        flag = False

        word = ""
        for char in line:
            if char == "\n":
                break
            elif char == " " and not flag:
                if word:
                    word_list.append(word)
                    word = ""
            else:
                word += char
                if char == "\'" or char == "\"":
                    if word and not flag:
                        word_list.append(word)
                        word = ""
                    flag = not flag

        if word_list[0][0] == '#':
            return []
        else:
            return word_list

    def next_word(self):
        if not word_list:
            self.line = self.file.readline()

            if not line:
                return None

            self.word_list = self.split(self.line)

        if word_list:
            return self.word_list.pop(0)

        # def char_accumulator(self):
        #     literal_char = "\'"

        #     while True:
        #         char = self.file.read(BYTE)
        #         literal_char += char
        #         if char == "\'":
        #             break
        #     return literal_char

        # def str_accumulator(self):
        #     literal_string = "\""

        #     while True:
        #         char = self.file.read(BYTE)
        #         literal_string += char
        #         if char == "\"":
        #             break
        #     return literal_string

        # def next_word(self):
        #     if self.accumulator:
        #         aux = self.accumulator
        #         self.accumulator = ""
        #         return aux

        #     word = ""
        #     while True:
        #         char = self.file.read(BYTE)

        #         if not char:
        #             break

        #         if char == " ":
        #             self.column += 1
        #             if word:
        #                 break
        #         elif char == "\n":
        #             self.line += 1
        #             self.column = 1
        #             if word:
        #                 break

        #         elif char == "\"":
        #             if not word:
        #                 return self.str_accumulator()
        #             else:
        #                 self.accumulator = self.str_accumulator()
        #                 break
        #         elif char == "\'":
        #             if not word:
        #                 return self.str_accumulator()
        #             else:
        #                 self.accumulator = self.char_accumulator()
        #                 break
        #         else:
        #             word += char

        #     return word
