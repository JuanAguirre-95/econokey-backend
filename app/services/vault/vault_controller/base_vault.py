import datetime
import uuid
from dataclasses import dataclass, field, asdict


@dataclass(init=True, repr=True)
class BaseVault:
    """
    Vault Structure Class
    """

    vault_name: str = field(init=True)
    vault_id: str = field(init=True)
    wallets: list[dict] = field(default_factory=list)
    notes: list[dict] = field(default_factory=list)
    passwords: list[dict] = field(default_factory=list)

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

    def add_password(self, element: dict):
        element["element_id"] = str(uuid.uuid4())
        self.passwords.append(element)

    def update_password(self, _id, element):
        for psw in self.passwords:
            if psw["element_id"] == _id:
                psw.update(element)

    def get_password(self, _id):
        for password in self.passwords:
            if password["element_id"] == _id:
                return password
        return None

    def delete_password(self, _id):
        for i, elem in enumerate(self.passwords):
            if elem["element_id"] == _id:
                return self.passwords.pop(i)

    def add_wallet(self, wallet: dict):
        wallet["element_id"] = str(uuid.uuid4())
        self.wallets.append(wallet)

    def update_wallet(self, _id, element):
        for wallet in self.wallets:
            if wallet["element_id"] == _id:
                wallet.update(element)

    def get_wallet(self, _id):
        for wallet in self.wallets:
            if wallet["element_id"] == _id:
                return wallet
        return None

    def delete_wallet(self, _id):
        for i, elem in enumerate(self.wallets):
            if elem["element_id"] == _id:
                return self.wallets.pop(i)

    def add_note(self, note: dict):
        note["element_id"] = str(uuid.uuid4())
        self.notes.append(note)

    def update_note(self, _id, element):
        for note in self.notes:
            if note["element_id"] == _id:
                note.update(element)

    def get_note(self, _id):
        for note in self.notes:
            if note["element_id"] == _id:
                return note
        return None

    def delete_note(self, _id):
        for i, elem in enumerate(self.notes):
            if elem["element_id"] == _id:
                return self.notes.pop(i)

    def get_dict(self):
        return asdict(self)
