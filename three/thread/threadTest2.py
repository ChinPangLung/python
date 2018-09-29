# 多进程和多线程最大的区别在于，多进程中，同一个变量，各自有一份拷贝在于每一个进程中，而多线程中，所有的变量有所有的线程共享，
# 所以任何一个变量的都可以被任意一个线程修改，因此线程之间共享数据最大的危险在于多个线程同时改一个变量。

# demo
import time, threading,multiprocessing

lock = threading.Lock() #锁

# 假定这是银行存款
balance = 0

def change_it(n):
    #先存后取,结果应该为0
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):
    start=time.time()
    for i in range(1000000):
        #修改前需要先获取锁
        lock.acquire()
        try:
            #只有拿到锁后才能进到try内，锁同一时刻只能最多一个线程获取到
            change_it(n)
        finally:
            #改完数据后记得释放锁
            lock.release()
    end=time.time()
    print('using time is %s '%((end-start)),threading.current_thread().name)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

print(multiprocessing.cpu_count())

