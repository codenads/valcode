from enum import Enum, auto

TOKENS = {
    'init': 'RW_INIT',
    '(': 'OP_PAR',
    ')': 'CL_PAR',
    '{': 'OP_CBRA',
    '}': 'CL_CBRA',
    '[': 'OP_BRA',
    ']': 'CL_BRA',
    'function': 'RW_FN',
    'int': 'RW_INT',
    'float': 'RW_FLOAT',
    'bool': 'RW_BOOL',
    'char': 'RW_CHAR',
    'null': 'RW_NULL',
    'void': 'RW_VOID',
    'string': 'RW_STR',
    'return': 'RW_RTN',
    'if': 'RW_IF',
    'else': 'RW_ELSE',
    'while': 'RW_WHILE',
    'for': 'RW_FOR',
    'var': 'RW_VAR',
    'and': 'RW_AND',
    'or': 'RW_OR',
    'not': 'RW_NOT',
    'input': 'RW_INPUT',
    'print': 'RW_PRINT',
    ':': 'SB_COLON',
    ';': 'SB_SCOLON',
    ',': 'SB_COMMA',
    '=': 'SB_ASGN',
    '+': 'OPR_ADD',
    '-': 'OPR_SUB',
    '*': 'OPR_MUL',
    '/': 'OPR_DIV',
    '//': 'OPR_FDIV',
    'ung': 'OPR_UNG',
    'ups': 'OPR_UPS',
    '==': 'OPR_EQUAL',
    '!=': 'OPR_UNEQ',
    '>': 'OPR_GT',
    '<': 'OPR_LT',
    '>=': 'OPR_GTE',
    '<=': 'OPR_LTE',
}


class TokenCategory(Enum):
    IDENTIFIER = auto()
    RW_INIT = auto()
    OP_PAR = auto()
    CL_PAR = auto()
    OP_CBRA = auto()
    CL_CBRA = auto()
    OP_BRA = auto()
    CL_BRA = auto()
    RW_FN = auto()
    RW_INT = auto()
    RW_FLOAT = auto()
    RW_BOOL = auto()
    RW_CHAR = auto()
    RW_NULL = auto()
    RW_VOID = auto()
    RW_STR = auto()
    RW_RTN = auto()
    RW_IF = auto()
    RW_ELSE = auto()
    RW_WHILE = auto()
    RW_FOR = auto()
    RW_VAR = auto()
    RW_AND = auto()
    RW_OR = auto()
    RW_NOT = auto()
    RW_INPUT = auto()
    RW_PRINT = auto()
    SB_COLON = auto()
    SB_SCOLON = auto()
    SB_COMMA = auto()
    SB_ASGN = auto()
    OPR_ADD = auto()
    OPR_SUB = auto()
    OPR_MUL = auto()
    OPR_DIV = auto()
    OPR_FDIV = auto()
    OPR_UNG = auto()
    OPR_UPS = auto()
    OPR_EQUAL = auto()
    OPR_UNEQ = auto()
    OPR_GT = auto()
    OPR_LT = auto()
    OPR_GTE = auto()
    OPR_LTE = auto()
    CT_INT = auto()
    CT_FLOAT = auto()
    CT_BOOL = auto()
    CT_CHAR = auto()
    CT_STR = auto()


class Token:
    def __init__(self, lexeme, token_enum):
        self.lexeme = lexeme  # 'function'
        self.token_enum = token_enum.value  # 3
        self.token_enum_category = token_enum.name  # FUNC
