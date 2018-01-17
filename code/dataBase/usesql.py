#-*-coding:utf-8-*-
import pymysql

db = pymysql.connect("localhost", "root", "123456", "my_db")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM t_novel"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        no = row[1]
        name = row[2]
        au = row[3]
        wanjie = row[4]
        print('id=%s,id=%s'%(id,id))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()