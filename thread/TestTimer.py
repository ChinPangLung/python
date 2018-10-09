#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午5:17
# @Author  : ChinPangLung
# @Site    : 
# @File    : TestTimer.py
# @Software: PyCharm

from threading import Timer
def hello():
    print('hello python')

timer = Timer(1, hello)
timer.start()

