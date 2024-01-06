import threading
import socket

nickname = input('Nhap ten: ')
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 1111)

client.sendto(nickname.encode('ascii'), server_address)

#Hàm để nhận và hiển thị tin nhắn từ máy chủ
# Function to receive messages from the server
def receive():
    while True:
        try:
            message, server_address = client.recvfrom(1024)
            message = message.decode('ascii')
            print(message)
        except:
            print("Da co loi xay ra!")
            client.close()
            break


# Hàm để nhập và gửi tin nhắn đến máy chủ
def write():
    while True:
        message = input("")
        client.sendto(f'{nickname}: {message}'.encode('ascii'), server_address)

#Tạo hai luồng riêng biệt để nhận và gửi tin nhắn
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
