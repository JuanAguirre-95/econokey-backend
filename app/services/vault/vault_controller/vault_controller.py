import dataclasses
import json
import os

from cryptography.fernet import Fernet

from app.services.vault.vault_controller.base_vault import BaseVault
from security import derive_key


class VaultController:

    def __init__(self):
        self.current_key = None
        self.open_vault: BaseVault = None

    def create_vault(self, vault_name: str, vault_key: str):
        """Create a new vault.
        :param vault_name: Vault name
        :param vault_key: Vault Key
        :return:
        """
        print("Creating new vault...")
        self.current_key = vault_key
        self.open_vault = BaseVault(vault_name)

    def load_vault(self, vault_name: str, vault_key: str) -> None:
        """
        Loads a vault in memory for accessing data
        :param vault_name: Vault name string.
        :param vault_key: Vault password.
        :return: None
        """
        print(f"Loading vault {vault_name}...")
        with open(f"vaults/{vault_name}.vault", "rb") as vault:
            # TODO: Implement safe filepath loading
            token = vault.readlines()
            salt = token[0].strip(str.encode("\n"))
            fermat = Fernet(derive_key(vault_key, salt))
            readable = fermat.decrypt(token[1])

            self.open_vault = BaseVault(**json.loads(readable))

    def save_vault(self, vault_name: str, vault_key: str):
        """
        Encrypts and flushes the vault to disk.
        :param vault_name: Vault name
        :param vault_key: Vault Key
        :return:
        """
        with open(f"vaults/{vault_name}.vault", "wb") as vault:
            # TODO: Implement safe filepath loading
            salt = os.urandom(16)
            fermat = Fernet(derive_key(vault_key, salt))
            content = json.dumps(self.open_vault.get_dict(), separators=(',',':'))
            not_readable = fermat.encrypt(str.encode(content))
            lines = [salt+str.encode("\n"), not_readable]
            vault.writelines(lines)

    def get_vault(self):
        """
        Fetch currently open vault.
        :return:
        """
        return self.open_vault


vault_cont = VaultController()
# vault_cont.load_vault("vault", "")
vault_cont.create_vault("Hola", "pizza")
vault_cont.get_vault().add_note({
      "note_name": "Agua",
      "contents": {
        "text": "Toma mas agua gato"
      }
    })
vault_cont.save_vault("Hola", "pizza")
vault_cont.load_vault("Hola", "pizza")
vault_cont.save_vault("Hola", "pizza")
print(vault_cont.get_vault())
