#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-10 上午9:41
# @Author  : ChinPangLung
# @Site    : 
# @File    : ProcessArray.py
# @Software: PyCharm
# 使用Array共享数据
from multiprocessing import Process, Array
import time


def foo(i, temp):
    temp[0] += 100
    for item in temp:
        if item == 22:
            time.sleep(0.1)
        print(i, '-------->', item)


if __name__ == '__main__':
    temp = Array('i', [11, 22, 33, 44])
    for i in range(2):
        process = Process(target=foo, args=(i, temp))
        process.start()
