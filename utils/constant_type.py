from token import TOKENS
import re


def is_integer(string):
    return re.match(r'[+-]?\d+$', string)


def is_float(string):
    return re.match(r'[+-]?\d+\.\d+', string)


def is_bool(string):
    return re.match(r'true|false', string)


def is_char(string):
    return re.match(r'^"."$', string)


def is_string(string):
    return re.match(r'^".*"$', string)


def is_identifier(string):
    return re.match(r'^[A-Za-z]+[A-Za-z0-9_]*', string)


def literal_constant_type(string):
    if is_integer(string):
        return ['CLT_INT', len(TOKENS) + 1]
    elif is_float(string):
        return ['CLT_FLOAT', len(TOKENS) + 2]
    elif is_bool(string):
        return ['CLT_BOOL', len(TOKENS) + 3]
    elif is_char(string):
        return ['CLT_CHAR', len(TOKENS) + 4]
    elif is_string(string):
        return ['CLT_STRING', len(TOKENS) + 5]
    elif is_identifier(string):
        return ['IDENTIFIER', len(TOKENS) + 6]
