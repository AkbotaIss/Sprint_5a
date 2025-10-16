import time
import random
import string

def email_plus_alias(base_email: str) -> str:
    name, domain = base_email.split("@", 1)
    stamp = int(time.time() * 1000)
    return f"{name}+{stamp}@{domain}"

def password_valid(length: int = 8) -> str:
    length = max(length, 6)
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choices(alphabet, k=length))

def password_short(length: int = 5) -> str:
    length = min(length, 5)
    alphabet = string.ascii_lowercase + string.digits
    return "".join(random.choices(alphabet, k=length))
