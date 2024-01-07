import threading
import socket

host = "127.0.0.1"
port = 1111

# Tạo một socket máy chủ và cấu hình của nó
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Gán địa chỉ IP vào cổng cho socket máy chủ
server.bind((host, port))

# Danh sách rỗng sẽ chưa các dối tượng địa chỉ IP của máy khách kết nối đến máy chủ
clients = set()

# Bản tin gủi đến các máy khách
def broadcast(message, client_address):
    for addr in clients:
        if addr != client_address:
            server.sendto(message, addr)

# Hàm để nhắn tin nhắn từ các máy khách
def receive():
    while True:
        message, client_address = server.recvfrom(1024)
        if client_address not in clients:
            print(f'Connected to: {str(client_address)}')
            clients.add(client_address)
            broadcast(message, client_address)

# Tạo một luồng để chạy chức năng nhận
receive_thread = threading.Thread(target=receive)
receive_thread.start()
