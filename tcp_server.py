import asyncio
import websockets
import json
import socket


def get_local_ip():
    # 创建一个 UDP 套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 连接到一个公共的 IP 地址，不会真正发送数据
        sock.connect(("8.8.8.8", 80))
        # 获取本地 IP 地址
        local_ip = sock.getsockname()[0]
    finally:
        # 关闭套接字
        sock.close()
    return local_ip


def handle_data():
    wd = "22"
    sd = "33"
    yw = "44"
    data = {
        "wd": wd,
        "sd": sd,
        "yw": yw
    }
    json_str = json.dumps(data)
    return json_str


async def handle_websocket(websocket, path):
    # 在此处理WebSocket连接
    async for message in websocket:
        # 处理接收到的消息
        print(f"接收到来自客户端的消息：{message}")
        # 数据获取
        json_str=handle_data()
        # 发送消息给客户端
        await websocket.send(json_str)
        print(f"向客户端发送消息：{json_str}")


IP = get_local_ip()  # 服务器的IP地址
PORT = 9000  # 服务器的端口号
# 创建WebSocket服务器
print("本地IP：", IP)
print("本地PORT：", PORT)


# 创建WebSocket服务器
start_server = websockets.serve(handle_websocket, IP, PORT)

# 启动服务器
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
