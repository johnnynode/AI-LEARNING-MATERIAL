# coding=utf-8

# 导入 pymysql 模块
import pymysql

# 获取数据库连接
db = pymysql.connect(host="localhost", user="root", password="123456", db="mydb", charset="utf8")


# 创建游标对象
cursor = db.cursor()

# 定义sql语句
sql = 'select * from stu'

# 执行sql语句
try:
    cursor.execute(sql)
    
    print('result ', cursor.rowcount)
    data1 = cursor.fetchone() # test 一条数据
    print(data1)
    
    print('all data')
    dataall = cursor.fetchall() # test 多条数据 两者同时使用会影响 fetchall 的结果
    print(dataall)
except:

    print('SQL执行错误!')

# 关闭数据库连接
db.close()
