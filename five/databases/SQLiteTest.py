# 导入数据库驱动
import sqlite3

# 连接到sqlite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建
connect = sqlite3.connect('test.db')
# 创建一个cursor 通过cursor执行sql语句，然后获取执行结果
cursor = connect.cursor()
# 执行一条sql语句，创建一个table
# cursor.execute('create table user (id varchar(20) primary key ,name varchar(20))')
# insert into data
for n in range(3, 10):
    cursor.execute("insert into user (id,name) values (?,?)", (str(n), 'long' + str(n)))
# 通过rowcount获取插入的行数
print(cursor.rowcount)
connect.commit()  # 记住这里，一定要提交
cursor.close()
connect.close()
