from multiprocessing import Pool
import os
import time
import random


def child_task(name):
    print('子进程 %s ID是：%s 正在运行' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)  # 随机休眠
    end = time.time()
    print('子进程:%s 运行了:%0.2f秒' % (name, (end - start)))


if __name__ == '__main__':
    print('当前父进程id是：%s'% os.getpid())
    p=Pool(4)#创建进程池实例，大小是4个进程
    for i in range(5):#循环5次，创建5个进程
        p.apply_async(child_task,args=(i,))
    print('子进程循环创建完毕，正在等待子进程执行')
    p.close()#关闭进程池，之后就不能添加新的进程了
    p.join()#如果有进程池，调用join前必须调用close。（join方法，等待所有子进程执行完毕再往下执行）
    print('所有进程运行完毕')

