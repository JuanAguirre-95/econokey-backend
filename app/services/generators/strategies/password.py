from dataclasses import dataclass
from typing import Any

from app.services.generators import factory


class PasswordGenerator:
    """Password generation"""

    generator_type: str = "password"

    def __init__(self, *args, **kwargs):
        """Instantiate the generation with the required parameters"""
        params: dict = kwargs.get("parameters", None)
        if params:
            for key, value in params.items():
                self.__setattr__(key, value)

    def generate(self, *args, **kwargs) -> Any:
        """
        Generate a new password with the specified parameters.
        :param args:
        :param kwargs:
        :return:
        """
        return "password"

    def get_defaults(self) -> dict:
        return {}


def register() -> None:
    factory.register("password", PasswordGenerator)
