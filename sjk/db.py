import sqlite3


# 打开数据库连接
def connect_database():
    conn = sqlite3.connect('test.db')
    return conn


# 创建表
def create_table(conn, table_name):
    conn = conn
    cursor = conn.cursor()
    sql_drop = 'drop table if exists ' + table_name
    #cursor.execute(sql_drop)
    sql_create = 'create table if not exists ' + table_name + '(addr varchar(50),' \
                                                              'power int,' \
                                                              'day date,' \
                                                              'time date,' \
                                                              'temp double(4,2),' \
                                                              'humi double(4,2),' \
                                                              'smok int,' \
                                                              'atti varchar(20),' \
                                                              'gps varchar(50),' \
                                                              'verify varchar(20)) '
    # 异常处理
    try:
        # 创建一个表格
        cursor.execute(sql_create)
        conn.commit()
    except:
        cursor.execute(sql_drop)
        conn.commit()



# 插入数据
def insert(conn, table_name, data):
    conn = conn
    cursor = conn.cursor()
    # 插入一条记录
    sql_insert = 'insert into ' + table_name + '(addr,power,day,time,temp,humi,smok,atti,gps,verify) values (?,?,?,?,?,?,?,?,?,?)'
    try:
        cursor.execute(sql_insert, data)
        conn.commit()
    except:
        print('insert error')


# 根据字段名查询数据
def select(conn, table_name, column_name):
    conn = conn
    cursor = conn.cursor()
    sql = 'select '+ column_name+' from '+table_name +' where time = (select max(time) from '+ table_name + ' where day = (select max(day) from '+table_name+'))'
    try:
        cursor.execute(sql)
        ret = cursor.fetchall()
        return ret
    except:
        print('unable to fetch data')
        return None



# 查询地址
def select_addr(conn, table_name):
    return select(conn, table_name, 'addr')


# 查询电量
def select_power(conn, table_name):
    return select(conn, table_name, 'power')


# 查询年月日
def select_day(conn, table_name):
    return select(conn, table_name, 'day')


# 查询时分秒
def select_time(conn, table_name):
    return select(conn, table_name, 'time')


# 查询温度
def select_temp(conn, table_name):
    return select(conn, table_name, 'temp')[0][0]


# 查询湿度
def select_humi(conn, table_name):
    return select(conn, table_name, 'humi')[0][0]


# 查询烟雾浓度
def select_smok(conn, table_name):
    return select(conn, table_name, 'smok')


# 查询姿态
def select_atti(conn, table_name):
    return select(conn, table_name, 'atti')


# 查询湿度
def select_gps(conn, table_name):
    return select(conn, table_name, 'gps')


# 修改数据
def update(conn, table_name, column_name, column, line_name, line_id):
    conn = conn
    cursor = conn.cursor()
    line = (line_name, line_id)
    sql_update = 'update '+table_name+' set '+column_name + '=? where '+column+' =?'
    try:
        cursor.execute(sql_update, line)
        conn.commit()
    except:
        conn.rollback()
        print('update error')


# 删除数据
def delete(conn, table_name, column_name, column):
    conn = conn
    cursor = conn.cursor()
    sql_delete = 'delete from '+table_name+' where '+column_name+' =?'
    column = (column,)
    try:
        cursor.execute(sql_delete, column)
        conn.commit()
    except:
        print('delete error')


# 关闭数据库连接
def close_connect(conn):
    conn = conn
    cursor = conn.cursor()
    cursor.close()
    conn.close()





