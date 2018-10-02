# 从wsigref模块导入
from wsgiref.simple_server import make_server
# 导入自己编写的application函数
from hello import application

server = make_server('', 8897, application)
print('server http on prot 8897')
server.serve_forever()

