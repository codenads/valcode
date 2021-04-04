from FileReader import FileReader
from Token import TOKENS, TokenCategory, Token


class LexicalAnalyzer:
    def __init__(self, file):
        self.file_reader = FileReader(file)
        self.remaining_token_start = 0

    def next_token(self):
        word = self.file_reader.read()
        token_column = self.file_reader.column - len(word)
        start = self.remaining_token_start

        print(word, start)

        if not word:
            return None
        if word in TOKENS.keys():
            return Token(self.file_reader.line, token_column, word, TokenCategory[TOKENS[word]])
        elif word[start: start+2] in TOKENS.keys():
            return Token(self.file_reader.line, token_column, word[start: start+2], TokenCategory[TOKENS[word[start: start+2]]])
        elif word[start] in TOKENS.keys():
            return Token(self.file_reader.line, token_column, word[start], TokenCategory[TOKENS[word[start]]])
        else:
            end = start + 1
            while end < len(word):
                print(word[start: end])
                if word[end] in TOKENS.keys() or word[end: end+2] in TOKENS.keys():
                    self.remaining_token_start = end
                    break
                end += 1

            if word[start: end] in TOKENS.keys():
                return Token(self.file_reader.line, token_column + start, TokenCategory[TOKENS[word[start: end]]])
