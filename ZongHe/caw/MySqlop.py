'''
数据库操作
'''

# 连接数据库
import pymysql


def connect(db):
    '''
    连接数据库
    :param db: db = {"ip":"jy001","port":4406,"dbName":"future","username":"root","pwd":"123456"}
    :return:
    '''
    host = db['ip']
    port = int(db['port'])
    user = db['username']
    name = db['dbName']
    pwd = db['pwd']
    try:
        conn = pymysql.connect(host=host, port=port, user=user, password=pwd, database=name, charset='utf8')
        print(f"连接数据库{host}:{port}成功")
    except Exception as e:
        print(f"连接数据库异常,异常信息为:{e}")
    return conn


# 断开数据库连接
def disconnect(conn):
    try:
        conn.close()
        print(f"断开数据库成功")
    except Exception as e:
        print(f"断开数据库连接失败,异常信息为:{e}")


# 执行sql语句
def execute(conn, sql):  # 连接相当于建了一条到数据库的路
    try:
        cursor = conn.cursor()  # 获取游标，相当于在路上跑的一辆车
        cursor.execute(sql)  # 执行sql语句
        conn.commit()  # 提交
        cursor.close()  # 关闭游标
        print(f"执行sql语句{sql}成功")
    except Exception as e:
        print(f"执行sql语句{sql}失败,异常信息为:{e}")


if __name__ == '__main__':
    db = {"ip": "jy001", "port": 4406, "dbName": "future", "username": "root", "pwd": "123456"}
    conn = connect(db)
    execute(conn, "delete from Member where mobilephone=18329586478;")
    disconnect(conn)
