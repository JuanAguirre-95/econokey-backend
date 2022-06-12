from typing import Any, Protocol


class BaseGenerator(Protocol):
    """Base class for Password, Passphrase and Wallets"""

    def generate(self, *args, **kwargs) -> Any:
        """
        Generic generate method
        :param args:
        :param kwargs:
        :return: Any
        """
    def get_defaults(self) -> dict:
        """
        Returns a dict containing default parameters for the class
        :return:
        """
