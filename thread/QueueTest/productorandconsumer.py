#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-10 上午9:16
# @Author  : ChinPangLung
# @Site    : 
# @File    : productorandconsumer.py
# @Software: PyCharm

import threading
import queue
import time

queue_queue = queue.Queue(10)


def productor(i):
    while True:
        queue_queue.put("生产者%s,生产了一个商品" % i)
        time.sleep(1)


def consumer(k):
    while True:
        print("消费者%s,消费了一个商品" % k)
        time.sleep(1)


for i in range(3):
    thread = threading.Thread(target=productor, args=(i,))
    thread.start()

for k in range(10):
    threading_thread = threading.Thread(target=consumer, args=(k,))
    threading_thread.start()

