from FileReader import FileReader
from Token import TOKENS, TokenCategory, Token
from CustomType import custom_type


class LexicalAnalyzer:
    def __init__(self, file):
        self.file_reader = FileReader(file)
        self.word = ""

    def next_token(self):
        if not self.word:
            self.word = self.file_reader.next_word()

        if not self.word:
            return None

        if self.word in TOKENS.keys():
            lexeme = self.word
            lexeme_column = self.file_reader.column
            self.word = ""
            self.file_reader.column += len(self.word)
            return Token(self.file_reader.line, lexeme_column, lexeme, TokenCategory[TOKENS[lexeme]])

        else:
            lexeme = ""
            end = 1

            if self.word[0] not in TOKENS.keys():
                while end < len(self.word):
                    if self.word[end] in TOKENS.keys():
                        break
                    end += 1

            lexeme = self.word[0: end]
            self.word = self.word[end:]

            self.file_reader.column += end

            if lexeme in TOKENS.keys():
                return Token(self.file_reader.line, self.file_reader.column, lexeme, TokenCategory[TOKENS[lexeme]])
            else:
                typeof = custom_type(lexeme)
                return Token(self.file_reader.line, self.file_reader.column, lexeme, TokenCategory[typeof])
