import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 1111))
server.listen()

clients = []
names = []

#Hàm để gửi tin nhắn đến tất cả các máy khách
def broadcast(message):
    for client in clients:
        client.send(message)

#Hàm xử lý kết nối của từng máy khách
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(f'{name} da roi khoi room chat!'.encode('ascii'))
            names.remove(name)
            break

#Hàm chấp nhận kết nối và quản lý các máy khách
def receive():
    while True:

        #Chấp nhận kết nối và lưu trữ địa chỉ IP của client
        client, address = server.accept()
        print(f"Ket noi voi {str(address)}")
        client.send(''.encode('ascii'))

        #Nhập tên của client và thêm vào danh sách
        name = client.recv(1024).decode('ascii')
        names.append(name)
        clients.append(client)

        #In ra tên của client đã kết nối
        print(f'Ten cua server la {name}')
        broadcast(f'{name} da vao phong chat! '.encode('ascii'))
        client.send('\nKet noi vao server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()