import threading
import socket

host = "127.0.0.1"
port = 1111

# Create a server socket and configure it
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

# An empty set to store the IP addresses of connected clients
clients = set()

# Function to broadcast messages to all clients
def broadcast(message, client_address):
    for addr in clients:
        if addr != client_address:
            server.sendto(message, addr)

# Function to receive messages from clients
def receive():
    while True:
        message, client_address = server.recvfrom(1024)
        if client_address not in clients:
            print(f'Connected to: {str(client_address)}')
            clients.add(client_address)
            broadcast(message, client_address)

# Create a thread to run the receive function
receive_thread = threading.Thread(target=receive)
receive_thread.start()
