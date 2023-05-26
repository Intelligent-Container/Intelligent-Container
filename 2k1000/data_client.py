import socket

# 定义服务器地址和端口
HOST = 'localhost'  # 服务器的IP地址或主机名
PORT = 8080  # 服务器的端口号

# 创建TCP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
client_socket.connect((HOST, PORT))

# 发送数据给服务器
message = "Hello, Server!"
client_socket.send(message.encode('utf-8'))

# 接收服务器的响应
response = client_socket.recv(1024)
if response:
    # 处理接收到的响应
    received_data = response.decode('utf-8')
    print(f"接收到来自服务器的响应：{received_data}")

# 关闭客户端套接字
client_socket.close()
