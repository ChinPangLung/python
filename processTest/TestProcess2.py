#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-10 上午9:33
# @Author  : ChinPangLung
# @Site    : 
# @File    : TestProcess2.py
# @Software: PyCharm

from multiprocessing import Process

list_1 = []


def foo(i):
    list_1.append(i)
    print("this is Process", i, "and list_1 is ", list_1)


if __name__ == '__main__':
    for i in range(5):
        process = Process(target=foo, args=(i,))
        process.start()
    print("the end list_1 is ", list_1)
