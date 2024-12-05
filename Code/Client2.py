import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Server's hostname or IP address
PORT = 65432        # Port used by the server

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT}")

def receive_messages():
    while True:
        try:
            # Receive message from the other client
            message = client_socket.recv(1024)
            if not message:
                print("Connection closed by the server.")
                break
            print(f"Friend: {message.decode()}")
        except:
            break

# Start a thread to listen for incoming messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

try:
    while True:
        # Send a message to the other client
        message = input()
        client_socket.sendall(message.encode())

        # Exit if the user types "exit"
        if message.lower() == 'exit':
            print("Exiting chat.")
            break
except:
    pass
finally:
    client_socket.close()
    print("Connection closed.")