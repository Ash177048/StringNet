from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import base64

BLOCK_SIZE = 16  # AES block size

def pad(data):
    pad_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    return data[:-data[-1]]

def get_key(string_key):
    return SHA256.new(string_key.encode()).digest()

def encrypt_message(message, string_key):
    key = get_key(string_key)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(message.encode()))
    return base64.b64encode(iv + ct_bytes)

def decrypt_message(enc_message, string_key):
    key = get_key(string_key)
    data = base64.b64decode(enc_message)
    iv = data[:BLOCK_SIZE]
    ct = data[BLOCK_SIZE:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct)).decode()
