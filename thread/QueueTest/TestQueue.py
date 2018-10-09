#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午5:22
# @Author  : ChinPangLung
# @Site    : 
# @File    : TestQueue.py
# @Software: PyCharm
# 先进先出队列

import queue

queue_queue = queue.Queue(5)
queue_queue.put(11)
queue_queue.put(22)
queue_queue.put(33)

print(queue_queue.get())
print(queue_queue.get())
print(queue_queue.get())
