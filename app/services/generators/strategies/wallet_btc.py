from dataclasses import dataclass
from typing import Any

from app.services.generators import factory


@dataclass
class WalletBTCGenerator:
    """BTC Wallet generation"""

    generator_type: str

    def __init__(self, *args, **kwargs):
        """Instantiate the generation with the required parameters"""
        params: dict = kwargs.get("parameters")
        for key, value in params.items():
            self.__setattr__(key, value)

    def generate(self, *args, **kwargs) -> Any:
        """
        Generate a new password with the specified parameters.
        :param args:
        :param kwargs:
        :return:
        """
        return "ALKSDNSDFG9UIZXKZOXCUIZB"


def register() -> None:
    factory.register("wallet_btc", WalletBTCGenerator)
