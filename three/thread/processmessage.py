from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def writer(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue...' % value)


if __name__ == '__main__':
    # 父进程创建queue，并传给各个子进程
    q = Queue()
    pw = Process(target=writer, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程，写入
    pw.start()
    # 启动子进程，读出
    pr.start()
    pw.join()  # 等待pw结束
    pr.terminate()  # 因为这里的pr里面是死循环逻辑，无法等待结束的，只能强行结束
