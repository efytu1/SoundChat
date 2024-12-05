# import socket

# # Server configuration
# HOST = '127.0.0.1'  # Localhost
# PORT = 65432        # Port to listen on (use ports > 1023)

# # Create a socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to the address and port
# server_socket.bind((HOST, PORT))

# # Listen for incoming connections
# server_socket.listen()
# print(f"Server is listening on {HOST}:{PORT}")

# # Accept a connection
# conn, addr = server_socket.accept()
# print(f"Connected by {addr}")

# # Handle client connection
# with conn:
#     while True:
#         # Receive message from client
#         client_message = conn.recv(1024)  # Buffer size 1024 bytes
#         if not client_message:
#             print("Client disconnected.")
#             break
#         print(f"Client: {client_message.decode()}")

#         # Send a response to the client
#         server_message = input("Server: ")
#         conn.sendall(server_message.encode())
import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (use ports > 1023)

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(2)
print(f"Server is listening on {HOST}:{PORT}")

clients = []

def handle_client(client_socket, other_client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                print("A client disconnected.")
                other_client_socket.sendall(b"Client disconnected.")
                break
            other_client_socket.sendall(message)
        except:
            break
    client_socket.close()

# Accept two client connections
for i in range(2):
    conn, addr = server_socket.accept()
    clients.append(conn)
    print(f"Client {i+1} connected by {addr}")

# Start threads to handle clients
thread1 = threading.Thread(target=handle_client, args=(clients[0], clients[1]))
thread2 = threading.Thread(target=handle_client, args=(clients[1], clients[0]))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

server_socket.close()