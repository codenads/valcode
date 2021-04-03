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
    return not re.search(r'[^A-Za-z0-9_]', string) and re.match(r'^[A-Za-z][A-Za-z0-9_]*', string)


def custom_type(string):
    if is_integer(string):
        return 'CT_INT'
    elif is_float(string):
        return 'CT_FLOAT'
    elif is_bool(string):
        return 'CT_BOOL'
    elif is_char(string):
        return 'CT_CHAR'
    elif is_string(string):
        return 'CT_STR'
    elif is_identifier(string):
        return 'IDENTIFIER'
