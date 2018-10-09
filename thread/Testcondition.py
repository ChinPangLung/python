#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午5:12
# @Author  : ChinPangLung
# @Site    : 
# @File    : Testcondition.py
# @Software: PyCharm

import threading


def condition():
    ret = False
    r = input(">>>")
    if r == "yes":
        ret = True
    return ret


def func(conn, i):
    print(i)
    conn.acquire()
    conn.wait_for(condition)  # 这个方法接受一个函数的返回值
    print(i + 100)
    conn.release()


c = threading.Condition()
for i in range(10):
    t = threading.Thread(target=func, args=(c, i,))
    t.start()
