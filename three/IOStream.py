# 基本概念：input output stream
# 存在问题：出入和接收速度不匹配
# 解决方法：同步、异步（回调，轮询）
# 新知：编程语言都会把底层的接口封装好。

# 读文件
try:
    file = open('/home/lung/Documents/vi/study', 'r')  # r表示读
    print(file.name)
    print(file.mode)

    print(file.read())
finally:
    if file:
        file.close()

print('===============================================')
# 简便写法
with open('/home/lung/Documents/vi/study', 'r') as f:  # 这种写法和前面的try....finally相同,不用写close()
    print(f.read())

# read(size)和readlines() errors='ignore'表示如果遇到编码错误的问题，直接忽略
with open('/home/lung/Documents/vi/study', 'r', encoding='utf-8', errors='ignore') as f1:
    for line in f1.readlines():
        print(line.strip())

# 读取图片
with open('/home/lung/图片/images.png', 'rb') as fb:  # rb表示读取二进制文件，例如图片
    print(fb.read())

# 写文件
try:
    fw = open('/home/lung/Documents/vi/study2', 'w')  # w表示写入文本文件(会覆盖原来的数据) wb表示写入二进制文件
    fw.write('我是写入的文本文件')
finally:
    if fw:
        fw.close()  # 只有调用close时，才能保证把全部数据写入到磁盘，因为有可能有部分数据是暂时放到内存缓冲区的

# ===============》
with open('/home/lung/Documents/vi/study3', 'w', encoding='utf-8') as fw2:
    fw2.write('我是with模式中，写入的中文文本数据')

with open('/home/lung/Documents/vi/study3', 'a', encoding='utf-8') as fa:  # a模式表示追加数据，不会覆盖原来的
    fa.write("我是a模式，追加的数据")
    fa.write('\n')
    fa.write("我是a模式，追加的数据")

# test demo
with open('/home/lung/Documents/vi/study', 'r') as fread:
    with open('/home/lung/Documents/vi/study4', 'w') as fwrite:
        fwrite.write(fread.read())
    print('END')

# StringIO就是表示在内存中读写str(文本对象)
from io import StringIO

# StringIO写操作
fio = StringIO()
print(fio.write('hello,world'))
print(fio.write(' '))
print(fio.getvalue())
# StringIO读写操作
print('========')
fiorw = StringIO('hello! \nHI!\nworld!')
while True:
    s = fiorw.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO表示在内存中操作二进制对象
from io import BytesIO

fbio = BytesIO()
print(fbio.write('中文'.encode('utf-8')))  # 这里不是写入str，而是写入了utf-8编码的bytes
print(fbio.getvalue())
fbio2=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(fbio2.read())

#操作文件和目录
import os
print(os.name)#系统类型
print(os.uname())#系统信息
print(os.environ)#环境变量
print(os.environ.get('HOME'))

#创建删除目录
print(os.path.abspath('.'))#查看当前文件的绝对路劲
#创建一个目录
join = os.path.join('/home/lung/PycharmProjects/python', 'testdir')
print(join)
os.mkdir(join)
#删除一个目录
os.rmdir(join)
#拆分路径
print(os.path.split(join))
#获取文件扩展名
print(os.path.splitext(join))
#重命名
#os.rename('/home/lung/Documents/vi/111','/home/lung/Documents/vi/test')
#删除文件
# os.remove('path')

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='py'])
