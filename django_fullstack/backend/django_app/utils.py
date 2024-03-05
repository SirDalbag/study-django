import random
import re


def generate_token(characters: str, length: int = 128):
    token = "".join(random.choice(characters) for _ in range(length))
    return token


def check_password(password: str) -> bool:
    pattern = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,16}$")
    return bool(pattern.match(password))
