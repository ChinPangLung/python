#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午5:25
# @Author  : ChinPangLung
# @Site    : 
# @File    : TestLifoQueue.py
# @Software: PyCharm
#后进先出队列 类似于“堆栈”，后进先出。也较常用。
import queue

lifo_queue = queue.LifoQueue()
lifo_queue.put(112)
lifo_queue.put(332)
print(lifo_queue.get())
print(lifo_queue.get())


