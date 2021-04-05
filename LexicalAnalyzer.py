from FileReader import FileReader
from Token import TOKENS, TokenCategory, Token
from CustomType import custom_type


class LexicalAnalyzer:
    def __init__(self, file):
        self.file_reader = FileReader(file)
        self.word = ""
        self.remaining_token_start = 0

    def next_token(self):
        if not self.remaining_token_start:
            self.word = self.file_reader.read()

        if not self.word:
            return None

        token_column = self.file_reader.column - len(self.word)
        start = self.remaining_token_start

        # print(word, start)

        if self.word in TOKENS.keys():
            self.remaining_token_start = 0
            return Token(self.file_reader.line, token_column, self.word, TokenCategory[TOKENS[self.word]])
        elif self.word[start: start+2] in TOKENS.keys():
            self.remaining_token_start += 2
            return Token(self.file_reader.line, token_column, self.word[start: start+2], TokenCategory[TOKENS[self.word[start: start+2]]])
        elif self.word[start] in TOKENS.keys():
            self.remaining_token_start += 1
            return Token(self.file_reader.line, token_column, self.word[start], TokenCategory[TOKENS[self.word[start]]])
        else:
            end = start + 1
            while end < len(self.word):
                if self.word[end] in TOKENS.keys() or self.word[end: end+2] in TOKENS.keys() and self.word[end: end+2] != 'or':
                    self.remaining_token_start = end
                    break
                end += 1

            if self.word[start: end] in TOKENS.keys():
                return Token(self.file_reader.line, token_column + start, self.word[start: end], TokenCategory[TOKENS[self.word[start: end]]])
            else:
                typeof = custom_type(self.word[start: end])
                return Token(self.file_reader.line, token_column + start, self.word[start: end], TokenCategory[typeof])
