import threading
import socket

nickname = input('Nhap ten: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1111))

client.send(nickname.encode('ascii'))

#Hàm để nhận và hiển thị tin nhắn từ máy chủ
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii') 
            print(message)
        except:
            print("Da co loi xay ra!")
            client.close()
            break

# Hàm để nhập và gửi tin nhắn đến máy chủ
def write():
    while True:
        message = input("")
        client.send(f'{nickname}: {message}'.encode('ascii'))

#Tạo hai luồng riêng biệt để nhận và gửi tin nhắn
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
