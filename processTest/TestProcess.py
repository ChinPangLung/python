#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-10 上午9:30
# @Author  : ChinPangLung
# @Site    : 
# @File    : TestProcess.py
# @Software: PyCharm

from multiprocessing import Process


def foo(i):
    print("this is Process", i)


if __name__ == '__main__':
    for i in range(5):
        p = Process(target=foo, args=(i,))
        p.start()
