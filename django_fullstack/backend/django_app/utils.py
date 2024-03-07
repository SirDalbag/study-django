import random
import re


def generate_token(characters: str, length: int = 128):
    token = "".join(random.choice(characters) for _ in range(length))
    return token


def check_password(password: str) -> bool:
    pattern = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,16}$")
    return bool(pattern.match(password))


def get_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
