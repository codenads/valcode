import re
from token import Token, TokenCategory, TOKENS
from utils.constant_type import custom_type
from utils.custom_split import custom_split


class lexical_analyzer:
    def next_token(self, word, start):

        if word[start: len(word)] in TOKENS.keys():
            # ex.: 'function'
            return Token(word[start: len(word)], TokenCategory[TOKENS[word[start: len(word)]]])

        elif word[start: start+2] in TOKENS.keys():
            # ex.: '==' or "!="
            return Token(word[start: start+2], TokenCategory[TOKENS[word[start: start+2]]])

        elif word[start] in TOKENS.keys():
            # ex.: ';'
            return Token(word[start], TokenCategory[TOKENS[word[start]]])

        else:
            # ex.: 'main()'
            end = start + 1
            while end < len(word):
                if word[end] in TOKENS.keys() or word[end: end+2] in TOKENS.keys():
                    break
                end += 1

            if word[start: end] in TOKENS.keys():
                return Token(word[start: end], TokenCategory[TOKENS[word[start: end]]])

            word_custom_type = custom_type(
                word[start: end])
            if word_custom_type:
                return Token(word[start:end], TokenCategory[word_custom_type])
            else:
                return None

    def parse_file(self, filename):
        line_count = 1

        file = open(filename, 'r')

        try:
            for line in file:
                line = line.replace('\n', '')
                print(f"{line_count:04d}  {line}")

                wordList = custom_split(line)

                current_line_position = 0

                for word in wordList:
                    current_word_letter = 0

                    while True:
                        token = self.next_token(word, current_word_letter)
                        if not token:
                            raise Exception(
                                f'Token error at line {line_count}, column {current_line_position + 1}.')
                        current_word_letter += len(token.lexeme)
                        column_count = line.find(
                            token.lexeme, current_line_position)
                        current_line_position = column_count + \
                            len(token.lexeme)
                        print(
                            f'{10*" "}[{line_count}, {column_count+1}] ({token.token_enum}, {token.token_enum_category}) {{{token.lexeme}}}')
                        if token.lexeme[-1] == word[-1]:
                            break
                line_count += 1

        except Exception as error:
            print(error)

        file.close()
