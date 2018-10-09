#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午5:00
# @Author  : ChinPangLung
# @Site    : 
# @File    : TestLock.py
# @Software: PyCharm

import threading
import time

NUM = 10


def func(lock):
    global NUM
    lock.acquire()  # 让锁开始起作用
    NUM -= 1
    time.sleep(1)
    print(NUM)
    lock.release()  # 释放锁


lock = threading.Lock()  # 实例化一个锁对象
for i in range(10):
    t = threading.Thread(target=func, args=(lock,))  # 记得把锁当作参数传递给func参数
    t.start()
# lock它不支持嵌套锁。RLcok类的用法和Lock一模一样，但它支持嵌套，因此我们一般直接使用RLcok类
