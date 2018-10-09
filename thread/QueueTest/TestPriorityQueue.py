#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午5:26
# @Author  : ChinPangLung
# @Site    : 
# @File    : TestPriorityQueue.py
# @Software: PyCharm
# 优先级队列 带有权重的队列，每个元素都是一个元组，前面的数字表示它的优先级，数字越小优先级越高，同样的优先级先进先出

import queue

priority_queue = queue.PriorityQueue()
priority_queue.put((2,'alex1'))
priority_queue.put((3,'alex2'))
priority_queue.put((1,'alex3'))
priority_queue.put((4,'alex4'))
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())
