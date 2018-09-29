import threading, time, random

from vboxapi import xrange


def show(num):
    print('线程%s 的结果是： %s ' % (threading.current_thread().name, num))


def test_add():
    # time.sleep(random.random() * 3)  # 随机休眠
    result = 0  # 线程的私有变量
    for _ in xrange(1000):  # 循环1000次，xrange返回的是生成器，range返回的是list，数据量大的时候用xrange
        result += 1
    show(result)  # 调用其他函数的时候，需要把私有变量传递过去


threads = []
for i in range(5):
    threads.append(threading.Thread(target=test_add, name=(i + 1)))  # 创建5个线程
    threads[i].start()
    # threads[i].join()

# ===================>>>>
print('===================>>>>')
data = {}  # 定义全局字典


def show1():  # 线程所调用函数不用接收参数，直接获取全局字典的值即可
    thread = threading.current_thread()  # 当前线程的实例
    print('线程__%s 的结果是：%s' % (thread.getName(), data[thread]))


def test_add1():
    thread = threading.current_thread()  # 当前线程的实例作为字典的key值
    data[thread] = 0  # 初始结果为0
    for _ in xrange(1000):
        data[thread] += 1
    show1()  # 此时调用其他函数，可不用传递参数
    # print(data.__len__())


threads1 = []
for i in range(5):
    threads1.append(threading.Thread(target=test_add1, name=(i + 1)))
    threads1[i].start()

print('<<==================>>')
data1 = threading.local()  # 获取ThreadLocal实例


def show2():
    thread = threading.current_thread()  # 当前的线程实例
    print('线程===%s的结果是：%s' % (thread.name, data1.num))  # 获取ThreadLocal实例value值data1.num（key值已经绑定）


def test_add2():
    data1.num = 0  # 直接给ThreadLocal实例添加num属性，并赋值为0，其实还可以赋值其他属性例如：data1.a data1.b
    for _ in xrange(1000):
        data1.num += 1
    show2()


threads2 = []
for i in range(5):
    threads2.append(threading.Thread(target=test_add2, name=(i + 1)))
    threads2[i].start()
print(data1)
print(type(data1))
