#coding : UTF-8

from pymysql import Connection
 

conn = Connection(
    host = "localhost",     # 主机（IP）
    port = 3306,            # 端口
    user = 'root',          # 账户
    password = '123456',    # 密码
    autocommit = True       # 插入数据自动提交，如果不设置要使用commit（）
)
print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('cgift')
# 运行sql代码
cursor.execute("CREATE TABLE FRIEND (NAME VARCHAR(10), AMOUNT INT)")

cursor.execute("SELECT * FROM COLLEAGUE")
# 获得DDL语言结果
res : tuple = cursor.fetchall()

for data in res:
    print(data)


conn.close()