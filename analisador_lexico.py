import re
from token import Token, TOKENS
from utils.constant_type import literal_constant_type
from utils.custom_split import custom_split


class analisador_lexico:

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

            literal_constant_object = literal_constant_check(
            ).literal_constant_type(word[start: end])
            if literal_constant_object:
                return Token(word[start: end], literal_constant_object[1], literal_constant_object[0])
            else:
                return Token(word[start: end], len(TOKENS) + 6, 'IDENTIFIER')
            print(literal_constant_object)
            # AQ
            # TODO mudar o 0 pra o valor certo de identifiers

    def read_whole_file(self, filename):
        line_count = 0

        file = open(filename, 'r')

        for line in file:
            if not line:
                break

            print(line.replace('\n', '').replace('\t', ''))
            wordList = custom_split(line.replace('\n', ''))

            for word in wordList:
                current_word_letter = 0

                while True:
                    token = self.nextToken(word, current_word_letter)
                    current_word_letter += len(token.lexeme)
                    column_count = line.find(token.lexeme)
                    print((10 * ' ') + str(line_count + 1) + ' ' + str(column_count + 1) + ' ' +
                          str(token.token_enum) + ' ' + token.token_enum_category + ' ' + token.lexeme)
                    if token.lexeme[-1] == word[-1]:
                        break
            #print('line_count = ' + str(line_count))
            line_count += 1
        file.close()
