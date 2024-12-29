import socket
import threading

# Server configuration
HOST = '10.15.245.226'
PORT = 65432

# List to store connected clients
clients = []

def handle_client(sender, receivers):
    """Receive messages from `sender` and broadcast them to `receivers`."""
    while True:
        try:
            # Receive message from the sender
            message = sender.recv(1024)
            if not message:
                print("A client disconnected.")
                break

            # Broadcast the message to all receivers
            for receiver in receivers:
                receiver.sendall(message)
        except Exception as e:
            print(f"Error handling client: {e}")
            break

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server running on {HOST}:{PORT}")

try:
    # Accept exactly three clients
    while len(clients) < 3:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        print(f"Client {address} connected.")

    print("All three clients connected. Starting communication.")

    # Create threads to manage communication
    thread1 = threading.Thread(target=handle_client, args=(clients[0], [clients[1], clients[2]]), daemon=True)
    thread2 = threading.Thread(target=handle_client, args=(clients[1], [clients[0], clients[2]]), daemon=True)
    thread3 = threading.Thread(target=handle_client, args=(clients[2], [clients[0], clients[1]]), daemon=True)

    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for threads to finish (optional; useful for cleanup)
    thread1.join()
    thread2.join()
    thread3.join()
except KeyboardInterrupt:
    print("Server shutting down.")
finally:
    for client in clients:
        client.close()
    server_socket.close()