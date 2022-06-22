from typing import Any

from app.services.generators import factory
from hdwallet import HDWallet
from hdwallet.utils import generate_mnemonic

class WalletGenerator:
    """BTC Wallet generation"""

    generator_type: str = "wallet"

    cryptocurrency: str = "BTC"
    wallet_name: str = f"{cryptocurrency} Wallet"

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

        mnemonic = generate_mnemonic("spanish")
        new_wallet = HDWallet(symbol=self.cryptocurrency)
        new_wallet.from_mnemonic(mnemonic=mnemonic)
        return {
            "passphrase": mnemonic,
            "private_key": new_wallet.private_key(),
            "public_key": new_wallet.public_key(),
            "wallet_name": self.wallet_name,
            "cryptocurrency": self.cryptocurrency
        }

    def get_defaults(self) -> dict:
        return {
            "generator_type": self.generator_type,
            "cryptocurrency": self.cryptocurrency,
            "wallet_name": self.wallet_name
        }


def register() -> None:
    factory.register("wallet", WalletGenerator)
