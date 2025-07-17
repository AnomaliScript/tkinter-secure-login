# Argon2, the Hashing + Salting tool
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def hash_password(password: str):
    return ph.hash(password)

def verify_password(stored_hash: str, attempt: str):
    try:
        return ph.verify(stored_hash, attempt)
    except VerifyMismatchError:
        return False