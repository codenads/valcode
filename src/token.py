from enum import Enum, auto

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
        self.lexeme = lexeme # 'function'
        self.token_enum = token_enum # 3
        self.token_enum_category = token_enum_category # FUNC
    