#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-10 上午9:58
# @Author  : ChinPangLung
# @Site    : 
# @File    : ProcessLock.py
# @Software: PyCharm
from multiprocessing import Process, queues, Array, RLock, Lock, Event, Condition, Semaphore
import multiprocessing
import time


def foo(i, li, lc):
    lc.acquire()
    li[0] = li[0] - 1
    time.sleep(1)
    print('say hi ', li[0])
    lc.release()


if __name__ == '__main__':
    li = Array('i', 1)
    li[0] = 10
    r_lock = RLock()
    for i in range(10):
        process = Process(target=foo, args=(i, li, r_lock))
        process.start()
