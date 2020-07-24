import string
import secrets
from itertools import cycle

LOWER_CASE = string.ascii_lowercase


class Cipher:
    def __init__(self, key=None):
        if key and isinstance(key, str):
            self.__key = key
        else:
            self.__key = self.__generate_key()

    @property
    def key(self):
        return self.__key

    @staticmethod
    def __generate_key(text=LOWER_CASE) -> str:
        return ''.join([LOWER_CASE[secrets.choice(range(0, len(LOWER_CASE)))] for char in text])

    def encode(self, text: str) -> str:
        new_text = list()
        for char, cipher in zip(text.lower(), cycle(self.__key)):
            index: int = LOWER_CASE.index(char)
            if index + LOWER_CASE.index(cipher) < len(LOWER_CASE):
                new_text.append(LOWER_CASE[index + LOWER_CASE.index(cipher)])
            else:
                new_text.append(LOWER_CASE[(index + LOWER_CASE.index(cipher)) - len(LOWER_CASE)])

        return ''.join(new_text)

    def decode(self, text: str) -> str:
        new_text = list()
        for char, cipher in zip(text.lower(), cycle(self.__key)):
            index: int = LOWER_CASE.index(char)
            new_text.append(LOWER_CASE[index - LOWER_CASE.index(cipher)])

        return ''.join(new_text)
