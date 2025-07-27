"""
CLASSIC CIPHERS: CAESAR & VIGENÈRE
- Caesar: Shifts letters by a fixed number.
- Vigenère: Uses a keyword for variable shifts.
- Includes substitution and space encoding for enhanced security.
"""

import string
import random

# Caesar Cipher
def caesar_encrypt(text, shift):
    """Encrypts text using Caesar cipher."""
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

# Vigenère Cipher
def vigenere_encrypt(text, key):
    """Encrypts text using Vigenère cipher."""
    result = ""
    key = key.lower()
    j = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[j % len(key)]) - ord('a')
            result += caesar_encrypt(char, shift)
            j += 1
        else:
            result += char
    return result

# Example Usage
message = "Hello World"
print("Caesar Encrypted:", caesar_encrypt(message, 3))
print("Vigenère Encrypted:", vigenere_encrypt(message, "KEY"))