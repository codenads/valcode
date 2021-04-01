from enum import Enum, auto

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


class TokenEnum(Enum):
    EOF = auto()
    ID = auto()
    FUNC = auto()
    INIT = auto()
    OP_PAR = auto()
    CL_PAR = auto()
    COLON = auto()
    SEMI_COLON = auto()
    OP_CURL_BRACKET = auto()
    CL_CURL_BRACKET = auto()
    INTEGER = auto()
    RETURN = auto()


class Token:
    def __init__(self, lexeme, token_enum, token_enum_category):
        self.lexeme = lexeme  # 'function'
        self.token_enum = token_enum  # 3
        self.token_enum_category = token_enum_category  # FUNC
