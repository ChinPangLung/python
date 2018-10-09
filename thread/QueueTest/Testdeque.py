#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午5:29
# @Author  : ChinPangLung
# @Site    : 
# @File    : Testdeque.py
# @Software: PyCharm
# 双向队列 Queue和LifoQueue的“综合体”，双向进出。方法较多，使用复杂，慎用！
import queue

q = queue.deque()
q.append(123)
q.append(333)
q.appendleft(456)
print(q.pop())
print(q.popleft())
