#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午5:08
# @Author  : ChinPangLung
# @Site    : 
# @File    : TestEvent.py
# @Software: PyCharm
import threading


def func(e, i):
    print(i)
    e.wait()  # 检测当前event是什么状态，如果是红灯，则阻塞，如果是绿灯则继续往下执行。默认是红灯。
    print(i + 100)


event = threading.Event()
for i in range(10):
    t = threading.Thread(target=func, args=(event, i))
    t.start()

event.clear()  # 主动将状态设置为红灯
inp = input(">>>")
if inp == "1":
    event.set()  # 主动将状态设置为绿灯
