class Token:
    def __init__(self, line, column, lexeme, token_enum):
        self.line = line
        self.column = column
        self.lexeme = lexeme
        self.token_name = token_enum.name
        self.token_value = token_enum.value

    def show(self):
        print(f'{10*' '}')
        print(f'[{self.line}, {self.column}]', end=" ")
        print(f'({self.token_name}, {self.token_value})' end=" ")
        print(f'{{{self.lexeme}}})
