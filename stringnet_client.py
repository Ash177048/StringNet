import socket
import threading
from crypto_utils import encrypt_message, decrypt_message

def receive_messages(sock, key):
    while True:
        try:
            data = sock.recv(2048)
            if data:
                try:
                    decrypted = decrypt_message(data, key)
                    print("\n>>", decrypted, "\n> ", end="")
                except:
                    print("\n>> [Decryption Failed]\n> ", end="")
        except:
            break

def main():
    HOST = input("Server IP (default: 127.0.0.1): ") or "127.0.0.1"
    PORT = 9999
    string_key = input("Enter shared string: ").strip()

    sock = socket.socket()
    sock.connect((HOST, PORT))
    sock.send((string_key + "\n").encode())

    threading.Thread(target=receive_messages, args=(sock, string_key), daemon=True).start()

    while True:
        msg = input("> ")
        enc = encrypt_message(msg, string_key)
        sock.send(enc)

if __name__ == "__main__":
    main()
