import socket
import threading

channels = {}  # string: [sockets]

def handle_client(conn, addr):
    try:
        string_key = conn.recv(1024).decode().strip()
        print(f"[{addr}] joined '{string_key}'")

        if string_key not in channels:
            channels[string_key] = []
        channels[string_key].append(conn)

        while True:
            data = conn.recv(2048)
            if not data:
                break
            for client in channels[string_key]:
                if client != conn:
                    try:
                        client.send(data)
                    except:
                        continue
    except:
        pass
    finally:
        channels[string_key].remove(conn)
        conn.close()

def main():
    HOST = '0.0.0.0'
    PORT = 9999

    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen()

    print(f"[Server] Listening on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
