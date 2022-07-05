"""Passphrase Generator Module"""
import random
from typing import Any

from app.services.generators import factory
from app.utils.wordlist import get_wordlist


class PassphraseGenerator:
    """
    Passphrase generation class
    """
    generator_type: str = "passphrase"
    word_count: int = 5
    delimiter: str = "."
    capitalization_type: str = "lowercase"
    word_pool: list = get_wordlist()
    delimiter_pool: str = ".,!@#$%^&*(){}:;"

    def __init__(self, *args, **kwargs):
        """Instantiate the generation with the required parameters"""
        params: dict = kwargs.get("parameters", None)
        if params:
            for key, value in params.items():
                self.__setattr__(key, value)

    def capitalization(self, capitalization: str, passphrase: list[str]) -> list[str]:
        """
        Applies capitalization type to elements in passphrase.
        :param capitalization: Capitalization type. lowercase, UPPERCASE and Capitalize
        :param passphrase: A list containing strings.
        :return: New list containing strings with applied capitalization.
        """
        match capitalization:
            case "Capitalize":
                return [word.capitalize() for word in passphrase]
            case "UPPERCASE":
                return [word.upper() for word in passphrase]

            case _:
                return [word.lower() for word in passphrase]

    def generate(self, *args, **kwargs) -> Any:
        """
        Generate a new passphrase with the specified parameters.
        :param args: not used
        :param kwargs: not used
        :return: A string containing n random word choices from a word pool and joined by specified delimiter
        """

        choices = random.choices(self.word_pool, k=self.word_count)
        choices = self.capitalization(self.capitalization_type, choices)
        if self.delimiter == "random":
            self.delimiter = random.choice(self.delimiter_pool)
        return {self.generator_type: self.delimiter.join(choices)}

    def get_defaults(self) -> dict:

        return {
            "word_count": self.word_count,
            "delimiter": self.delimiter,
            "capitalization_type": self.capitalization_type,
        }


def register() -> None:
    factory.register("passphrase", PassphraseGenerator)
