import sjk.db as db
import time
import sjk.uart as uart
import sjk.data_parse as d
import threading
from queue import Queue
import sjk.export_data as export_data


def main(conn):
    conn = db.connect_database()
    print("start db")
    table_name = time.strftime("D%Y_%m_%d", time.localtime())
    q = Queue()
    t1 = threading.Thread(target=uart.recv_data, args=(q,))
    t1.start()

    # json_str = '{"A":"start","B":"00:01:1B:FF:FF:FF","C":"100","D":["2023","05","06"],"E":["16", "26", "25"],"F":{"F1":"23.02","F2":"26","F3":"0","F4":"26&12&98","F5":"112.342473&16.842207"},"G":"12345678","H":"end"}'
    while True:
        #str = uart.recv_data()
        str1 = q.get()
        str2 = str1.decode("utf-8")
        flag = isinstance(str2, str)
        try:
            if flag:
                json_str = eval(str2)
                d_list = d.data_parse(json_str)
                if d_list[0] == "start" and d_list[len(d_list) - 1] == "end":
                    del d_list[0]
                    del d_list[len(d_list) - 1]
                    d_list[2] = time.strftime("%Y-%m-%d", time.localtime())
                    d_list[3] = time.strftime("%H:%M:%S", time.localtime())
                    data = tuple(d_list)
                    db.create_table(conn, table_name)
                    db.insert(conn, table_name, data)
                    ret = db.select_time(conn, table_name)
                    if ret:
                        print(ret[0][0])
            export_data.export_excel()

            wd = str(db.select_temp(conn, "D2023_05_24"))
            sd = str(db.select_humi(conn, "D2023_05_24"))
        except  Exception as e:
            print(e)

            print("except ")
            pass
    t1.join()
    db.close_connect(conn)


if __name__ == '__main__':
    conn = db.connect_database()
    main(conn)

