import random
import string
from dataclasses import dataclass
import secrets
from typing import Any

from app.services.generators import factory


class PasswordGenerator:
    """Password generation"""

    generator_type: str = "password"
    lenght: int = 10
    upper = True
    lower = True
    digit = True
    symbol = True

    lowercase: str = string.ascii_lowercase
    uppercase: str = string.ascii_uppercase
    digits: str = string.digits
    symbols: str = string.punctuation

    def __init__(self, *args, **kwargs):
        """Instantiate the generation with the required parameters"""
        params: dict = kwargs.get("parameters", None)
        if params:
            for key, value in params.items():
                self.__setattr__(key, value)

    def get_symbol_pool(self):
        pool: str = ""
        if self.upper:
            pool += self.uppercase
        if self.lower:
            pool += self.lowercase
        if self.digits:
            pool += self.digits
        if self.symbol:
            pool += self.symbols
        return pool

    def generate(self, *args, **kwargs) -> Any:
        """
        Generate a new password with the specified parameters.
        :param args:
        :param kwargs:
        :return:
        """
        pool = self.get_symbol_pool()
        splt = [c for c in pool]
        random.shuffle(splt)
        pool = "".join(splt)
        password = ''.join(secrets.choice(pool) for i in range(self.lenght))
        return password

    def get_defaults(self) -> dict:

        return {
            "lower": self.lower,
            "upper": self.upper,
            "digit": self.digit,
            "symbol": self.symbol,
            "lenght": self.lenght,
        }


def register() -> None:
    factory.register("password", PasswordGenerator)
