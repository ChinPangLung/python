import os

# windowns 中没有fork()，可以用muliprocessing模块的process
from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print('子进程 %s,ID是：%s' % (name, os.getpid()))


print('当前进程（父进程）的ID是：%s' % os.getpid())
p = Process(target=run_proc, args=('test',))  # 创建Process的实例，并传入子进程要执行的函数和参数
p.start()  # 子进程开始
p.join()  # join方法用于进程之间的同步，等待进程执行完再往下执行
print('子进程执行完毕，回到主进程%s' % os.getpid())

print('Process (%s) start....' % os.getpid())  # os.getpid()返回的是进程的id不是线程

pid = os.fork()  # 创建子进程，并返回进程的id，父进程返回的是父进程的id，而子进程返回的是0
if pid == 0:
    print('I am child process (%s) and parent is %s' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s)' % (os.getppid(), pid))
