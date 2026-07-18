import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)
print(f"chars {chars}")
print(f"key   {key}")

# Encrypt
while True:
    plain_text = input("Enter a message to encrypt: ")
    ciper_text = ""

    # EXIT OUT OF PROGRAMME
    if plain_text == "q":
        break

    for letter in plain_text:
        index = chars.index(letter)
        ciper_text += key[index]

    print(f"Original message: {plain_text}")
    print(f"Encrypted message: {ciper_text}")

    # Decrypt
    ciper_text = input("Enter a message to decrypt: ")
    plain_text = ""

    # EXIT OUT OF PROGRAMME
    if ciper_text == "q":
        break

    for letter in ciper_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Encrypted message: {ciper_text}")
    print(f"Original message: {plain_text}")