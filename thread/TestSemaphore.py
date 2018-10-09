#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午5:03
# @Author  : ChinPangLung
# @Site    : 
# @File    : TestSemaphore.py
# @Software: PyCharm

import time
import threading


def run(n):
    semaphore.acquire()
    print('run the thread: %s ' % n)
    time.sleep(1)
    semaphore.release()


num = 0
semaphore = threading.BoundedSemaphore(5)  # 允许最多5个线程同时进行

for i in range(20):
    thread = threading.Thread(target=run, args=(i,))
    thread.start()
