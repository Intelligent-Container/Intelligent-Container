import serial


def recv_data(q):
    # 打开串口
    ser = serial.Serial('COM6', 115200, timeout=1)  # “COM1”是Windows的串口
    # ser = serial.Serial('/dev/ttyS1', 9600, timeout=1) # '/dev/ttyS1'对应龙芯派 8pin为UART3_TX，10pin为UART3_RX，9pin为GND
    # ser = serial.Serial('/dev/ttyS2', 9600, timeout=1) # '/dev/ttyS2'对应龙芯派 53pin为UART4_TX，54pin为UART4_RX，57和58pin为GND
    # ser = serial.Serial('/dev/ttyS3', 115200, timeout=1)  # '/dev/ttyS3'对应龙芯派 55pin为UART5_TX，56pin为UART5_RX，57和58pin为GND
    # 接收数据并发送回去
    while True:
        data = ser.readline()
        if data:
            # return data.decode("utf-8")
            # print(data.decode("utf-8"))
            print(data)# 打印数据

            q.put(data)
