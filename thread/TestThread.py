#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午4:58
# @Author  : ChinPangLung
# @Site    : 
# @File    : TestThread.py
# @Software: PyCharm

import threading
import time

NUM = 0


def show():
    global NUM
    NUM += 1
    name = t.getName()
    time.sleep(1)  # 注意，这行语句的位置很重要，必须在NUM被修改后，否则观察不到脏数据的现象。
    print(name, "执行完毕后，NUM的值为： ", NUM)


for i in range(10):
    t = threading.Thread(target=show)
    t.start()
print('main thread stop')
