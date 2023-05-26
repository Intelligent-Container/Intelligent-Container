import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

import threading
from threading import Timer
import datetime

import sjk_test
import sqlite3
import sjk.db as db

sign = False  # 文字开关

window_width = 1024
window_height = 600

col_num = 11
row_num = 14

cell_width = int(window_width / col_num)
cell_height = int(window_height / row_num)

YW = "75 %"
ZT = "10—90—45"
WD = "25 ℃"
SD = "50 %"
TIME = "00:00:00"

exit_flag = False



def update_data(user):
    conn = sqlite3.connect('./test.db')
    global YW, ZT, WD, SD

    get_yw = sjk_test.send_yw()
    get_zt = sjk_test.send_zt()
    get_wd = sjk_test.send_wd()
    get_sd = sjk_test.send_sd()

    YW = str(get_yw) + "%"
    ZT = str(get_zt)
    WD = str(round(db.select_temp(conn, "D2023_05_24"), 2))
    SD = str(get_sd)

    user.label_yw_value.set_text(YW)
    user.label_zt_value.set_text(ZT)
    user.label_wd_value.set_text(WD)
    user.label_sd_value.set_text(SD)

    t = Timer(1, update_data, (user,))
    if exit_flag:
        t.cancel()
    t.start()
    t.join()


def on_window_close(window):
    global exit_flag
    exit_flag = True
    sjk_test.exit_flag = True
    Gtk.main_quit()


def change_size_color(label, size, color):
    css_str = "label {font-size:" + str(size) + "px; color: " + color + ";}"
    # 创建一个CSS Provider对象
    css_provider = Gtk.CssProvider()
    # 加载CSS样式文件
    css_provider.load_from_data(css_str.encode('utf-8'))
    # 创建一个Style Context对象，并应用CSS样式
    style_context = label.get_style_context()
    style_context.add_provider(css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)


def printTime(user):
    global TIME
    TIME = get_current_time()
    user.label_time.set_text(TIME)

    t = Timer(1, printTime, (user,))
    t.start()
    if exit_flag:
        t.cancel()
    t.join()



def get_current_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%Y年%m月%d日-%H时%M分%S秒")
    return time_str


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="一个页面")
        self.set_default_size(window_width, window_height)

        fixed = Gtk.Fixed()
        self.add(fixed)

        # 加载背景图片
        pix_buf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="./image/bg.png",
            width=window_width,
            height=window_height,
            preserve_aspect_ratio=True)
        image = Gtk.Image.new_from_pixbuf(pix_buf)
        fixed.put(image, cell_width * 0, cell_height * 0)

        if sign:
            label_yw = Gtk.Label(label="烟雾")
            change_size_color(label_yw, 40, "#000000")
            label_yw.set_size_request(cell_width * 2, cell_height)
            fixed.put(label_yw, cell_width * 1, cell_height * 5 + 15)

            label_zt = Gtk.Label(label="姿态")
            change_size_color(label_zt, 40, "#000000")
            label_zt.set_size_request(cell_width * 2, cell_height)
            fixed.put(label_zt, cell_width * 1, cell_height * 10 + 15)

            label_sd = Gtk.Label(label="湿度")
            change_size_color(label_sd, 40, "#000000")
            label_sd.set_size_request(cell_width * 2, cell_height)
            fixed.put(label_sd, cell_width * 8, cell_height * 5 + 15)

            label_wd = Gtk.Label(label="温度")
            change_size_color(label_wd, 40, "#000000")
            label_wd.set_size_request(cell_width * 2, cell_height)
            fixed.put(label_wd, cell_width * 8, cell_height * 10 + 15)

        self.label_yw_value = Gtk.Label(label=YW)
        change_size_color(self.label_yw_value, 25, "#FF0000")

        self.label_zt_value = Gtk.Label(label=ZT)
        change_size_color(self.label_zt_value, 20, "#FF0000")

        self.label_wd_value = Gtk.Label(label=WD)
        change_size_color(self.label_wd_value, 20, "#FF0000")

        self.label_sd_value = Gtk.Label(label=SD)
        change_size_color(self.label_sd_value, 20, "#FF0000")

        self.label_time = Gtk.Label(label=TIME)
        change_size_color(self.label_time, 20, "#0000FF")

        self.label_yw_value.set_size_request(cell_width * 2, cell_height)
        self.label_zt_value.set_size_request(cell_width * 2, cell_height)
        self.label_wd_value.set_size_request(cell_width * 2, cell_height)
        self.label_sd_value.set_size_request(cell_width * 2, cell_height)
        self.label_time.set_size_request(cell_width * 3, cell_height)

        fixed.put(self.label_yw_value, cell_width * 1, cell_height * 7 + 15)
        fixed.put(self.label_zt_value, cell_width * 1, cell_height * 12 + 15)
        fixed.put(self.label_wd_value, cell_width * 8, cell_height * 7 + 15)
        fixed.put(self.label_sd_value, cell_width * 8, cell_height * 12 + 15)
        fixed.put(self.label_time, cell_width * 4, cell_height * 2 + 5)


def main_fun():

    win = MainWindow()
    win.connect("destroy", on_window_close)
    win.show_all()

    # 创建并启动新线程
    thread_timer = threading.Thread(target=printTime, args=(win,))
    thread_timer.start()

    thread_update = threading.Thread(target=update_data, args=(win,))
    thread_update.start()

    thread_sjk = threading.Thread(target=sjk_test.refresh_data, args=(None,))
    thread_sjk.start()

    Gtk.main()
    # 等待新线程完成
    thread_timer.join()


if __name__ == '__main__':

    main_fun()
