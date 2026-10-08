"""Infer tablename from classname."""

from re import Pattern, compile as re_compile
from string import ascii_uppercase
from typing import Final

SIBILING_WORD_ENDING: Final[Pattern[str]] = re_compile(
    pattern=r'(?:c|s|x|z|sh|ch|zh)$',
)


def pascal_case_to_snake_case(string: str) -> str:
    """Convert a string in PascalCase to snake_case."""

    return ''.join(
        f'_{letter.lower()}' if letter in ascii_uppercase else letter
        for letter in string
    )[1:]


def classname_to_tablename(classname: str) -> str:
    """Infer tablename from classname."""

    if len(classname) == 0:
        raise ValueError('classname must not be empty')
    snaked_classname: str = pascal_case_to_snake_case(classname)
    if snaked_classname.endswith('y'):
        return f'{snaked_classname[:-1]}ies'
    if SIBILING_WORD_ENDING.search(snaked_classname) is not None:
        return f'{snaked_classname}es'
    return f'{snaked_classname}s'
