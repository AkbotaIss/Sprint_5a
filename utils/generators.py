import uuid
import random
import string

def make_email(prefix="Issina_Akbota_31_567", domain="ya.ru"):
    return f"{prefix}_{uuid.uuid4().hex[:6]}@{domain}"

def make_password_valid(length: int = 10):
    pool = string.ascii_letters + string.digits
    core_len = max(6, length)
    return "".join(random.choices(pool, k=core_len))

def make_password_short():
    return "12345"
