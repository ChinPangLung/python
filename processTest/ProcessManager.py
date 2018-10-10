#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-10 上午9:50
# @Author  : ChinPangLung
# @Site    : 
# @File    : ProcessManager.py
# @Software: PyCharm
# 使用Manager共享数据
from multiprocessing import Process, Manager
import time
import random


def foo(i, dic):
    dic[i] = 100 + i
    time.sleep(random.random())
    print(dic.values())


if __name__ == '__main__':
    manager = Manager()
    manager_dict = manager.dict()
    for i in range(10):
        process = Process(target=foo, args=(i, manager_dict))
        process.start()
        process.join()
