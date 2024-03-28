import string
import random

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_punctuation=True):
    """
    Generate a random password with the specified criteria.

    Args:
        length (int): The desired length of the password (default is 12).
        include_uppercase (bool): Whether to include uppercase letters (default is True).
        include_lowercase (bool): Whether to include lowercase letters (default is True).
        include_digits (bool): Whether to include digits (default is True).
        include_punctuation (bool): Whether to include punctuation (default is True).

    Returns:
        str: The generated random password.
    """
    characters = ""

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
print("Random Password:", generate_password())
print("Random Password (16 characters, no punctuation):", generate_password(length=16, include_punctuation=False))
print("Random Password (8 characters, only digits):", generate_password(length=8, include_uppercase=False, include_lowercase=False, include_punctuation=False))