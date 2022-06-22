import json
import os

from cryptography.fernet import Fernet

from app.models.vault import Vault
from app.services.vault.vault_controller.base_vault import BaseVault
from .security import derive_key

vault_dir = os.path.join(os.getcwd(), "vaults")
if not os.path.isdir(vault_dir):
    os.mkdir(vault_dir)


class VaultController:
    """Handles creation of a new vault file, loading and saving operations"""

    def __init__(self):
        self.open_vault: BaseVault = None

    def create_vault(self, vault_data: Vault):
        """Create a new vault file"""
        print("Creating new vault...")
        self.open_vault = BaseVault(vault_name=vault_data.vault_name, vault_id=vault_data.vault_id)
        self.save_vault(vault_data)

    def load_vault(self, vault_data: Vault) -> None:
        """
        Loads a vault in memory for accessing data
        :param vault_data:
        :return: None
        """
        print(f"Loading vault {vault_data.vault_name}...")
        with open(f"{vault_dir}/{vault_data.vault_name}.vault", "rb") as vault:
            token = vault.readlines()
            fernet = Fernet((derive_key(vault_data.vault_key, vault_data.salt)))
            readable = fernet.decrypt(token[0])

            self.open_vault = BaseVault(**json.loads(readable))

    def save_vault(self, vault_data: Vault):
        """
        Encrypts and flushes the vault to disk.
        :return:
        """
        print(vault_dir)
        with open(f"{vault_dir}/{vault_data.vault_name}.vault", "wb") as vault:
            fermat = Fernet(derive_key(vault_data.vault_key, vault_data.salt))
            content = json.dumps(self.open_vault.get_dict(), separators=(',', ':'))
            not_readable = fermat.encrypt(str.encode(content))
            lines = [not_readable]
            vault.writelines(lines)

    def get_vault(self):
        """
        Fetch currently open vault.
        :return:
        """
        return self.open_vault
