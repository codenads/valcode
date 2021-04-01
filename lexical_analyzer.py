import re
from token import Token, TOKENS
from utils.constant_type import literal_constant_type
from utils.custom_split import custom_split


class lexical_analyzer:
    def nextToken(self, word, start):
        whole_word = word[start: len(word)]

        if whole_word in TOKENS.keys():
            # ex.: 'function'
            return Token(whole_word, list(TOKENS.keys()).index(whole_word) + 1, TOKENS[whole_word])
        elif word[start] in TOKENS.keys():
            # ex.: ';'
            return Token(word[start], list(TOKENS.keys()).index(word[start]) + 1, TOKENS[word[start]])
        else:
            # ex.: 'main()'
            end = start + 1
            while end < len(word):
                if word[end] in TOKENS.keys():
                    break
                end += 1
            if word[start: end] in TOKENS.keys():
                return Token(word[start: end], list(TOKENS.keys()).index(word[start: end]) + 1, TOKENS[word[start: end]])

            literal_constant_object = literal_constant_type(word[start: end])
            if literal_constant_object:
                return Token(word[start:end], literal_constant_object[1], literal_constant_object[0])
                print(literal_constant_object)
            else:
                return None

    def serialize_line(self, line):
        return line.replace('\n', '')

    def parse_file(self, filename):
        line_count = 1

        file = open(filename, 'r')

        try:
            for line in file:
                line = self.serialize_line(line)
                print(f"{line_count:04d}  {line}")
                wordList = custom_split(line)
                current_line_position = 0

                for word in wordList:
                    current_word_letter = 0

                    while True:
                        token = self.nextToken(word, current_word_letter)
                        if not token:
                            raise Exception(
                                f'Token error at line {line_count}, column {column_count}.')
                        current_word_letter += len(token.lexeme)
                        column_count = line.find(
                            token.lexeme, current_line_position)
                        current_line_position = column_count
                        print(
                            f'{10*" "}[{line_count}, {column_count+1}]  ({token.token_enum}, {token.token_enum_category}) {{{token.lexeme}}}')
                        if token.lexeme[-1] == word[-1]:
                            break

                line_count += 1

        except Exception as error:
            print(error)

        file.close()
