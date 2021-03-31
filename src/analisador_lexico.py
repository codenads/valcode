import re
from token import Token

class literal_constant_check:
    def is_integer(string):
        return string.match(r'[+-]?\d+$')
    def is_float(string):
        return string.match(r'[+-]?\d+\.\d+')
    def is_bool(string):
        return string.match(r'[true|false]')
    def is_char(string):
        return string.match(r'[^"."$]')
    def is_string(string):
        return string.match(r'[^".*"$]/')
    
    def literal_constant_type(string):
        if is_integer(string):
            return 'CLT_INT'
        elif is_float(string):
            return 'CLT_FLOAT'
        elif is_bool(string):
            return 'CLT_BOOL'
        elif is_char(string):
            return 'CLT_CHAR'
        elif is_string(string):
            return 'CLT_STRING'



def custom_split(str_to_split):
    ignore_flag = False
    word_acc = ""
    str_acc = ""
    word_list = []
    for letter in str_to_split:
        if ignore_flag:
            str_acc += letter
            if letter == '"':
                ignore_flag = False
                word_list.append(str_acc)
                str_acc = ""
        else:
            if letter == ' ':
                if word_acc:
                    word_list.append(word_acc)
                    word_acc = ""
            elif letter == '"':
                str_acc += letter
                ignore_flag = True
            else:
                word_acc += letter
    if word_acc:
        word_list.append(word_acc)
    return word_list



    




class analisador_lexico:

    TOKENS = {
        'function': 'FUNCTION',
        'init': 'INIT',
        '(': 'OP_PARENTHESIS',
        ')': 'CL_PARENTHESIS',
        '{': 'OP_CURLY_BRACKET',
        '}': 'CL_CURLY_BRACKET',
        '[': 'OP_BRACKET',
        ']': 'CL_BRACKET',
        'int': 'INTEGER',
        'float': 'FLOAT',
        'bool': 'BOOLEAN',
        'char': 'CHARACTER',
        'null': 'NULL',
        'void': 'VOID',
        'string': 'STRING',
        'return': 'RETURN',
        'if': 'IF',
        'var': 'VAR',
        'else': 'ELSE',
        'while': 'WHILE',
        'for': 'FOR',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        ':': 'COLON',
        ';': 'SEMICOLON',
        ',': 'COMMA',
        '=': 'EQUAL',
        '-': 'SUBTRACTION',
        '+': 'ADDITION',
        '/': 'DIVISION',
        '*': 'MULTIPLICATION',
        '//': 'FLR_DIVISION',
    }

    def nextToken(self, word, start):
        whole_word = word[start: len(word)]

        if whole_word in self.TOKENS.keys():
            # ex.: 'function'
            return Token(whole_word, list(self.TOKENS.keys()).index(whole_word), self.TOKENS[whole_word])
        elif word[start] in self.TOKENS.keys():
            # ex.: ';'
            return Token(word[start], list(self.TOKENS.keys()).index(word[start]), self.TOKENS[word[start]])
        else:
            # ex.: 'main()'
            end = start + 1
            while end < len(word):
                if word[end] in self.TOKENS.keys():
                    break
                end += 1
            if word[start: end] in self.TOKENS.keys():
                return Token(word[start: end], list(self.TOKENS.keys()).index(word[start: end]), self.TOKENS[word[start: end]])
            #word_type = literal_constant_check.literal_constant_type()
            return Token(word[start: end], 0, word[start: end]) #AQ
            # TODO mudar o 0 pra o valor certo de identifiers

    def read_whole_file(self, filename):
        line_count = 0

        file = open(filename, 'r')

        for line in file:
            if not line:
                break

            print(line.replace('\n', ''))
            wordList = custom_split(line.replace('\n', ''))

            for word in wordList:
                current_word_letter = 0

                while True:
                    token = self.nextToken(word, current_word_letter)
                    current_word_letter += len(token.lexeme)
                    column_count = line.find(token.lexeme)
                    print((10 * ' ') + str(line_count) + ' ' + str(column_count) + ' ' + 
                        str(token.token_enum) + ' ' + token.token_enum_category + ' ' + token.lexeme)
                    if token.lexeme[-1] == word[-1]:
                        break
            #print('line_count = ' + str(line_count))
            line_count += 1
        file.close()