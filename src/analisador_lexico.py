import re
from token import Token

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
    'input': 'INPUT',
    'print': 'PRINT',
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

class literal_constant_check:
    def is_integer(self, string):
        return re.match(r'[+-]?\d+$', string)
    def is_float(self, string):
        return re.match(r'[+-]?\d+\.\d+', string)
    def is_bool(self, string):
        return re.match(r'true|false', string)
    def is_char(self, string):
        return re.match(r'^"."$', string)
    def is_string(self, string):
        return re.match(r'^".*"$', string)
    
    def literal_constant_type(self, string):
        if self.is_integer(string):
            return ['CLT_INT', len(TOKENS) + 1]
        elif self.is_float(string):
            return ['CLT_FLOAT', len(TOKENS) + 1]
        elif self.is_bool(string):
            return ['CLT_BOOL', len(TOKENS) + 1]
        elif self.is_char(string):
            return ['CLT_CHAR', len(TOKENS) + 1]
        elif self.is_string(string):
            return ['CLT_STRING', len(TOKENS) + 1]



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
                if word_acc:
                    word_list.append(word_acc)
                    word_acc = ""
            else:
                word_acc += letter
    if word_acc:
        word_list.append(word_acc)
    print('word_list', word_list)
    return word_list


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

            literal_constant_object = literal_constant_check().literal_constant_type(word[start: end])
            if literal_constant_object:
                return Token(word[start: end], literal_constant_object[1], literal_constant_object[0])
            else:
                return Token(word[start: end], len(TOKENS) + 6, 'IDENTIFIER')    
            print(literal_constant_object)
             #AQ
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