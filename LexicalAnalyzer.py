from FileReader import FileReader
from Token import TOKENS, TokenCategory, Token
from CustomType import custom_type


class LexicalAnalyzer:
    def __init__(self, file):
        self.file_reader = FileReader(file)
        self.word = None

    def next_token(self):
        if not self.word:
            self.word = self.file_reader.next_word()

        if not self.word:
            return None

        if self.word.lexeme in TOKENS.keys():
            lexeme = self.word.lexeme
            spaces = self.word.spaces
            column = self.file_reader.column

            self.file_reader.column += len(lexeme)
            self.word = None

            return Token(self.file_reader.line, column + spaces, lexeme, TokenCategory[TOKENS[lexeme]])

        else:
            end = 1

            if self.word.lexeme[0] in ["\'", "\""]:
                end = len(self.word.lexeme)
            elif self.word.lexeme[0] not in TOKENS.keys():
                while end < len(self.word.lexeme):
                    if self.word.lexeme[end] in TOKENS.keys():
                        break
                    end += 1

            lexeme = self.word.lexeme[0: end]
            spaces = self.word.spaces

            self.word.lexeme = self.word.lexeme[end:]

            if not self.word.lexeme:
                self.word = None

            if lexeme:
                column = self.file_reader.column
                self.file_reader.column += end

                if lexeme in TOKENS.keys():
                    return Token(self.file_reader.line, column + spaces, lexeme, TokenCategory[TOKENS[lexeme]])
                else:
                    typeof = custom_type(lexeme)
                    return Token(self.file_reader.line, column + spaces, lexeme, TokenCategory[typeof])
