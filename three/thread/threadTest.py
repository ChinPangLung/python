# python的线程是真正的Posix，Thread，而不是模拟出来的
# python标准库提供了_thread和_threading。_threading是高级模块，_thread是低级模块，在绝大多数的情况下，我们只要使用_threading就行了

# 启动一个线程就是把一个函数传入并且创建Tread实例，然后调用start()开始执行：
import time, threading


# 新线程执行的代码
# threading.current_thread()永远返回当前线程的实例
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thead %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended....' % threading.current_thread().name)


print('thread %s is running' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)


