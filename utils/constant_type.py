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


def custom_type(string):
    if is_integer(string):
        return 'CL_INT'
    elif is_float(string):
        return 'CL_FLOAT'
    elif is_bool(string):
        return 'CL_BOOL'
    elif is_char(string):
        return 'CL_CHAR'
    elif is_string(string):
        return 'CL_STR'
    elif is_identifier(string):
        return 'IDENTIFIER'
