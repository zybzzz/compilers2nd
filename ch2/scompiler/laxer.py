from io import open
from typing import Dict, TextIO
from mtoken import *


class Lexer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, file: str) -> None:
        self.file: TextIO = open(file, 'r')
        self.peek: str = " "
        self.words: Dict[str, Word] = {}

    def reverse(self, word: Word) -> None:
        self.words[word.lexeme] = word

