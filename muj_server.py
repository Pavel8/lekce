import socket
import threading

HOST = '127.0.0.1'
PORT = 12349

clients = []

def broadcast(message, client_socket):
    """Odošle správu všetkým pripojeným klientom okrem odosielateľa."""
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket):
    """Spracováva prichádzajúce správy od klienta."""

    try:
        client_socket.send("Zadajte názov miestnosti, do ktorej sa chcete pripojiť: ".encode())
        room_name = client_socket.recv(1024).decode().strip()

        if room_name not in clients:
            clients[room_name] = []

        clients[room_name].append(client_socket)
        print(f"Klient pripojený do miestnosti: {room_name}")

    # Oznámenie ostatným členom miestnosti
        broadcast(f"Nový člen sa pripojil do miestnosti {room_name}".encode(), client_socket, room_name)

    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
            else:
                break
        except:
            break

    client_socket.close()
    clients.remove(client_socket)

def main():
    """Hlavná funkcia na spustenie servera."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Server beží...")

    while True:
        client_socket, addr = server.accept()
        print(f"{addr} sa pripojil.")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
