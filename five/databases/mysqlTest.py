# pip3 install mysql-connector
# 导入mysql驱动

import mysql.connector

connect = mysql.connector.connect(user='root', password='root', database='test')
cursor = connect.cursor()

#create table
createSql='''create table user (id varchar(20) primary key ,name varchar(64))'''
cursor.execute(createSql)

#insert into data
insertSql='''insert into user (id,name) values (%s,%s)'''
cursor.execute(insertSql,['1','龙展鹏'])
connect.commit()
rowcount = cursor.rowcount
print(rowcount)
#query data
querySql='''select * from user where id =%s'''
cursor.execute(querySql, ('1',))
fetchall = cursor.fetchall()
print(fetchall)
cursor.close()
connect.close()

