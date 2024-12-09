'''
from ollama import Client
client = Client(
  host='http://localhost:11434',
  headers={'x-some-header': 'some-value'}
)
response = client.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
'''


import socket
import threading
from ollama import chat
from ollama import ChatResponse
from ollama import Client

# Server configuration
HOST = '127.0.0.1'  # Server's hostname or IP address
PORT = 65432        # Port used by the server

# Create a socket
observer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
observer_socket.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT}")

client = Client(
  host='http://localhost:11434',
  headers={'x-some-header': 'some-value'}
)
response = client.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])

def observe():
    while True:
        try:
            # Receive message from the other clients
            getMessage = observer_socket.recv(1024)
            if not getMessage:
                print("Connection closed by the server.")
                break
            response = client.chat(model='llama3.2', messages=[
                {
                    'role': 'user',
                    'content': f'Describe the sentiment of this sentence with one of (high positive, low positive, high negative, low negative) : {getMessage.decode()}',
                },
            ])
            print(response.message.content)
        except:
            break

# Start a thread to listen for incoming messages
observer_thread = threading.Thread(target=observe, daemon=True)
observer_thread.start()

# The client will only observe; no input or sending of messages.
try:
    # Keep the main thread alive to allow observation
    observer_thread.join()
except KeyboardInterrupt:
    print("Exiting observer mode.")
finally:
    observer_socket.close()
    print("Connection closed.")