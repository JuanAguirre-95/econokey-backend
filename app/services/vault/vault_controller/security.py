from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def derive_key(password: str, salt: bytes) -> bytes:
    """
    Derive 32-bit key from a text password with the provided salt
    :param password: A string that will be used to derive a new key
    :param salt: 16-bytes salt
    :return: URL-Safe encoded key
    """

    byte_key = str.encode(password)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = urlsafe_b64encode(kdf.derive(byte_key))
    return key
