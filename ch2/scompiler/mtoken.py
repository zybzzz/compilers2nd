from numbers import Number, Real
from commom import readonly_property
from enum import Enum
from typing import Union


class Tags(Enum):
    AND, BASIC, BREAK, DO, ELSE = 256, 257, 258, 259, 260
    EQ, FALSE, GE, ID, IF = 261, 262, 263, 264, 265
    INDEX, LE, MINUS, NE, NUM = 266, 267, 268, 269, 270
    OR, REAL, TEMP, TRUE, WHILE = 271, 272, 273, 274, 275


class Tag:
    def __init__(self, tag: Tags) -> None:
        self._tag: Tags = tag

    @readonly_property
    def tag(self) -> Tags:
        return self._tag

    def __str__(self) -> str:
        return str(self._tag)


class Num(Tag):
    def __init__(self, tag: Tags, value: Union[Number, Real]) -> None:
        super().__init__(self, tag)
        self._value: Union[Number, Real] = value

    @readonly_property
    def value(self) -> Number:
        return self._value

    def __str__(self) -> str:
        return str(self._value) + "   with tag  " + super().__str__()


class Word(Tag):

    def __init__(self, tag: Tags, lexeme: str) -> None:
        super().__init__(self, tag)
        self._lexeme: str = lexeme

    @readonly_property
    def lexeme(self) -> str:
        return self._lexeme

    def __str__(self) -> str:
        return str(self._lexeme) + "   with tag  " + super().__str__()


class PreWords:
    AND, OR, EQ = Word(Tags.AND, "&&"), Word(Tags.OR, "||"), Word(Tags.EQ, "==")
    NE, LE, GE = Word(Tags.NE, "!="), Word(Tags.LE, "<="), Word(Tags.GE, ">=")
    MINUS = Word(Tags.MINUS, "minus")
    TRUE = Word(Tags.TRUE, "true")
    FALSE = Word(Tags.FALSE, "false")
    TEMP = Word(Tags.TEMP, "t")
