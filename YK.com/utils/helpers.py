import random
import string
from datetime import datetime

def get_current_timestamp(fmt="%H%M%S_%d%m%Y"):
    """Возвращает текущую метку времени для логов, файлов и т.д."""
    return datetime.now().strftime(fmt)

def random_string(length=8):
    """Генерация случайной строки из букв."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_email():
    """Генерация случайного email."""
    name = random_string(6).lower()
    domain = random.choice(['example.com', 'mail.com', 'test.org'])
    return f"{name}@{domain}"

def random_phone():
    """Генерация рандомного российского телефона."""
    return "+7" + ''.join(random.choices("0123456789", k=10))

def normalize_text(text):
    """Приводит текст к нижнему регистру без пробелов по краям."""
    return text.strip().lower()
