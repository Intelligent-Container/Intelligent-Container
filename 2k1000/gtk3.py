import gi
from threading import Timer
import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

YW = "75 %"
ZT = "10—90—45"
WD = "25 ℃"
SD = "50 %"
TIME = "00:00:00"


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="船舶状态显示系统")
        self.set_default_size(1024, 600)

        # 加载背景图片
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="./image/bg.png",
            width=1024,
            height=600,
            preserve_aspect_ratio=True)

        image = Gtk.Image.new_from_pixbuf(pixbuf)

        # 创建一个11行14列的网格布局
        grid = Gtk.Grid()
        grid.set_row_homogeneous(True)
        grid.set_column_homogeneous(True)
        self.add(grid)

        # 创建一个标签，并将其放置在网格布局中间位置
        label_YW = Gtk.Label()
        p = f"<span font_desc='18' foreground='#c06f98' >烟雾:</span>\n"
        label_YW.set_markup(p)

        label_YW_Value = Gtk.Label()
        p = f"<span font_desc='18' foreground='#c06f98'  >{YW}</span>\n"
        label_YW_Value.set_markup(p)


        label_ZT = Gtk.Label()
        p = f"<span font_desc='18' foreground='#fcff38' >姿态:</span>\n"
        label_ZT.set_markup(p)

        label_ZT_Value = Gtk.Label()
        p = f"<span font_desc='18' foreground='#c06f98'  >{ZT}</span>\n"
        label_ZT_Value.set_markup(p)

        label_WD = Gtk.Label()
        p = f"<span font_desc='18' foreground='#fcff38' >温度:</span>\n"
        label_WD.set_markup(p)

        label_WD_Value = Gtk.Label()
        p = f"<span font_desc='18' foreground='#c06f98'  >{WD}</span>\n"
        label_WD_Value.set_markup(p)

        label_SD = Gtk.Label()
        p = f"<span font_desc='18' foreground='#fcff38' >湿度:</span>\n"
        label_SD.set_markup(p)


        label_SD_Value = Gtk.Label()
        p = f"<span font_desc='18' foreground='#c06f98'  >{SD}</span>\n"
        label_SD_Value.set_markup(p)

        self.label_TIME = Gtk.Label()
        p = f"<span font_desc='14' foreground='#fb0e0e'  >{TIME}</span>\n"
        self.label_TIME.set_markup(p)


        # 创建一个标签，设置其文本居中对齐
        #label = Gtk.Label()
        #label.set_text("Hello World")
        #p = f"<span font_desc='14' foreground='#fb0e0e'  >{TIME}</span>\n"
        #label.set_markup(p)
        # label.set_halign(Gtk.Align.CENTER)
        # label.set_valign(Gtk.Align.CENTER)

        # 将标签添加到网格布局中间位置
        #grid.attach(label, 5, 7, 1, 3)


        # label = Gtk.Label(label="Hello")

        # grid.attach(label, 6, 5, 2, 1)
        # grid.attach(label_YW, 1, 5, 2, 2)
        grid.attach(label_YW_Value, 1, 7, 2, 2)

        # grid.attach(label_ZT, 1, 10, 2, 2)
        grid.attach(label_ZT_Value, 1, 12, 2, 2)
        label_ZT_Value.set_halign(Gtk.Align.CENTER)
        label_ZT_Value.set_valign(Gtk.Align.CENTER)


        # grid.attach(label_WD, 8, 5, 2, 2)
        grid.attach(label_WD_Value, 8, 7, 2, 2)

        # grid.attach(label_SD, 8, 10, 2, 2)
        grid.attach(label_SD_Value, 8, 12, 2, 2)

        grid.attach(self.label_TIME, 3, 2, 5, 2)

        grid.attach(image, 0, 0, 11, 14)

# hour01 = 0
# hour02 = 0
# minute01 = 0
# minute02 = 0
# second01 = 0
# second02 = 0


def printTime(user):
    # global hour01, minute01, second01
    # print()
    # second01 += 1
    # if second01 == 60:
    #     minute01 += 1
    #     second01 = 0
    #     if minute01 == 60:
    #         hour01 += 1
    #         minute01 = 0
    #         if hour01 == 24:
    #             hour01 = 0
    # TIME = str(hour01).zfill(2) + ":" + str(minute01).zfill(2) + ":" + str(second01).zfill(2)
    TIME = get_current_time()
    p = f"<span font_desc='13' foreground='#c06f98' >{TIME}</span>\n"
    user.label_TIME.set_markup(p)
    # user.label_TIME.set_valign(Gtk.Align.CENTER)

    t = Timer(1, printTime, (user,))
    t.start()



def get_current_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%Y年%m月%d日-%H时%M分%S秒")
    return time_str


if __name__ == '__main__':
    win = MyWindow()
    # win.set_default_size(1024, 600)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    printTime(win)
    Gtk.main()
