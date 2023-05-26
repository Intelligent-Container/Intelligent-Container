import threading
from threading import Timer

yw = 0
zt = 0
wd = 0
sd = 0

exit_flag = False


def send_yw():
    return yw


def send_zt():
    return zt


def send_wd():
    return wd


def send_sd():
    return sd


def refresh_data(no):
    global yw, zt, wd, sd
    yw = yw + 1
    zt = zt + 2
    wd = wd + 3
    sd = sd + 4

    # print(send_yw())
    # print(send_zt())
    # print(send_wd())
    # print(send_sd())

    t = Timer(1, refresh_data, (None,))
    if exit_flag:
        t.cancel()
    t.start()
    t.join()


if __name__ == '__main__':
    # 创建并启动新线程
    thread_sjk = threading.Thread(target=refresh_data, args=(None,))
    thread_sjk.start()
    thread_sjk.join()
