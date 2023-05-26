import socket

# 定义服务器地址和端口
HOST = 'localhost'  # 可以是服务器的IP地址或主机名
PORT = 8080  # 自定义端口号

# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址和端口
server_socket.bind((HOST, PORT))

# 开始监听客户端连接
server_socket.listen()

print(f"服务器正在监听 {HOST}:{PORT} 上的连接...")

while True:
    # 接受客户端连接
    client_socket, client_address = server_socket.accept()
    print(f"客户端 {client_address} 已连接")

    # 接收客户端发送的数据
    data = client_socket.recv(1024)
    if data:
        # 处理接收到的数据
        received_data = data.decode('utf-8')
        print(f"接收到来自客户端的数据：{received_data}")

        # 发送响应给客户端
        response = "Hello, Client!"
        client_socket.send(response.encode('utf-8'))

    # 关闭与客户端的连接
    client_socket.close()
