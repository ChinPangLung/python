import sqlite3

connect = sqlite3.connect('test.db')
cursor = connect.cursor()
print(type(cursor))
# execute = cursor.execute('select * from user where id=?', ('1',))
sql='''select * from user '''
# execute = cursor.execute('select * from user')
result = cursor.execute(sql)
print(result)
all_user = result.fetchall()
print(all_user)
cursor.close()
connect.close()
