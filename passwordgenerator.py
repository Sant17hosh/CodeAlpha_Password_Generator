import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine character sets based on complexity options
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Check if the character set is empty
    if not all_chars:
        raise ValueError("Cannot generate a password with no character options.")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Usage example
password = generate_password(length=12, use_digits=True, use_special_chars=True)
print("Generated Password:", password)
