from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

KEY_FILE = "secret.key"

def generate_key():
    key = get_random_bytes(32)  # AES-256
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

key = load_key()

def encrypt_file(input_file, output_file):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(input_file, "rb") as f:
        data = f.read()

    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open(output_file, "wb") as f:
        f.write(cipher.nonce + tag + ciphertext)

def decrypt_file(input_file, output_file):
    with open(input_file, "rb") as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    with open(output_file, "wb") as f:
        f.write(data)
