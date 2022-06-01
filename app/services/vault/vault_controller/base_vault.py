import datetime
from dataclasses import dataclass, field, asdict


@dataclass(init=True, repr=True)
class BaseVault:
    """
    Vault Structure Class
    """

    vault_name: str
    open_time: datetime.datetime = field(default_factory=datetime.datetime.utcnow)
    wallets: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    passwords: list = field(default_factory=list)

    def list_passwords(self) -> list:
        """
        Return a list of saved passwords.
        :return:
        """
        return self.passwords

    def list_wallets(self) -> list:
        """
        Return a list of saved wallets.
        :return:
        """
        return self.wallets

    def list_notes(self) -> list:
        """
        Return a list of saved notes.
        :return:
        """
        return self.notes

    def add_password(self, password: dict):
        self.passwords.append(password)

    def add_wallet(self, wallet: dict):
        self.wallets.append(wallet)

    def add_note(self, note: dict):
        self.notes.append(note)

    def get_dict(self):
        return asdict(self)
