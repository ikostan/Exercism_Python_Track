import string
import secrets

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
        text: str = text.lower()
        new_text = list()

        if len(text) == len(self.__key):
            for char, cipher in zip(text, self.__key):
                index: int = LOWER_CASE.index(char)
                if index + LOWER_CASE.index(cipher) < len(LOWER_CASE):
                    new_text.append(LOWER_CASE[index + LOWER_CASE.index(cipher)])
                else:
                    new_text.append(LOWER_CASE[(index + LOWER_CASE.index(cipher)) - len(LOWER_CASE)])
        else:
            cipher = 0
            for char in text:
                index: int = LOWER_CASE.index(char)
                if index + LOWER_CASE.index(self.__key[cipher]) < len(LOWER_CASE):
                    new_text.append(LOWER_CASE[index + LOWER_CASE.index(self.__key[cipher])])
                else:
                    new_text.append(LOWER_CASE[(index + LOWER_CASE.index(self.__key[cipher])) - len(LOWER_CASE)])

                cipher += 1
                if cipher >= len(self.__key):
                    cipher = 0

        return ''.join(new_text)

    def decode(self, text: str) -> str:
        text: str = text.lower()
        new_text = list()

        if len(text) == len(self.__key):
            for char, cipher in zip(text, self.__key):
                index: int = LOWER_CASE.index(char)
                new_text.append(LOWER_CASE[index - LOWER_CASE.index(cipher)])
        else:
            cipher = 0
            for char in text:
                index: int = LOWER_CASE.index(char)
                new_text.append(LOWER_CASE[index - LOWER_CASE.index(self.__key[cipher])])

                cipher += 1
                if cipher >= len(self.__key):
                    cipher = 0

        return ''.join(new_text)
