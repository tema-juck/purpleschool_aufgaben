"""Генератор паролей"""
# import random
# import string


# def generate_password(length: int = 8, use_symbols: bool = True):
#     if length < 3:
#         return ""
#     letters = string.ascii_letters
#     numbers = string.digits
#     symbols = "!@#$%&*?"
#     pool = letters + numbers + symbols if use_symbols else letters + numbers
#     password_chars: list[str] = []

#     while len(password_chars) < length:
#         password_chars.append(random.choice(pool))

#     return "".join(password_chars)


# print(generate_password(6))
# print(generate_password(length=10))


def is_palindrome(text: str) -> bool:
    # Ваш код здесь
    normalized = text.lower().replace(" ", "")
    reversed_normalized = normalized[::-1]
    return True if normalized == reversed_normalized else False
    


# Примеры вызовов для проверки
print(is_palindrome("radar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("race car"))
