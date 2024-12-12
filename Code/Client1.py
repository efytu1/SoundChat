'''
import socket

# Server configuration
HOST = '127.0.0.1'  # Server's hostname or IP address
PORT = 65432        # Port used by the server

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT}")

# Send and receive data
try:
    while True:
        # Send a message to the server
        client_message = input("Client: ")
        client_socket.sendall(client_message.encode())

        # Exit loop if the user types "exit"
        if client_message.lower() == 'exit':
            print("Exiting chat.")
            break

        # Receive a response from the server
        server_message = client_socket.recv(1024)  # Buffer size 1024 bytes
        print(f"Server: {server_message.decode()}")
finally:
    client_socket.close()
    print("Connection closed.")
'''


import socket
import threading

# Server configuration
HOST = '10.15.245.226'  # Server's hostname or IP address
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


'''
import socket
import threading
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Define stems dictionary
stems = {
    "808": 'Stems/808-Bass-Scared_Confused.wav',
    "bell-a": 'Stems/Bell-Anxious.wav',
    "kick-a": 'Stems/Kick-Aggressive.wav',
    "kick-p": 'Stems/Kick-Pulse-Tense_Excited.wav',
    "p1": 'Stems/Percussion1.wav',
    "p2": 'Stems/Percussion2.wav',
    "p3": 'Stems/Percussion3.wav',
    "p4": 'Stems/Percussion4.wav',
    "p6": 'Stems/Percussion6.wav',
    "snare-t": 'Stems/Snare-Tense.wav',
    "snare2": 'Stems/Snare2.wav',
    "snare3": 'Stems/Snare3-Confused.wav',
    "sa": 'Stems/Synth-Accent-Tense_Confused.wav',
    "sa1": 'Stems/Synth-Accent1-Tense_Confused.wav',
    "sa3": 'Stems/Synth-Accent3_Confused.wav',
    "sa4": 'Stems/Synth-Accent4_Percussion5-Confused.wav',
    "sa5": 'Stems/Synth-Accent5-Confused.wav',
}

playing_sounds = {}

def toggle_stem(key, volume=1.0, fade_duration=1000):
    if key in stems:
        if key in playing_sounds:
            playing_sounds[key].fadeout(fade_duration)
            del playing_sounds[key]
        else:
            try:
                sound = pygame.mixer.Sound(stems[key])
                sound.set_volume(volume)
                sound.play(loops=-1, fade_ms=fade_duration)
                playing_sounds[key] = sound
            except pygame.error as e:
                print(f"Error loading sound: {e}")
    else:
        print(f"Key '{key}' not found in stems!")
    display_playing_sounds()

def display_playing_sounds():
    if playing_sounds:
        print("Currently playing sounds:")
        for key in playing_sounds.keys():
            print(f" - {key}")
    else:
        print("No sounds are currently playing.")

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

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
            message = message.decode()
            print(f"Friend: {message}")

            # Toggle stem if the message is a stem key
            toggle_stem(message)
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

        # Toggle stem if the message is a stem key
        toggle_stem(message)

        # Exit if the user types "exit"
        if message.lower() == 'exit':
            print("Exiting chat.")
            break
except:
    pass
finally:
    client_socket.close()
    pygame.mixer.quit()
    print("Connection closed.")
'''
