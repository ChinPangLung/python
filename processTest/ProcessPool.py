#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-10 上午10:05
# @Author  : ChinPangLung
# @Site    : 
# @File    : ProcessPool.py
# @Software: PyCharm
from multiprocessing import Pool
import time


def foo(args):
    time.sleep(1)
    print(args)


if __name__ == '__main__':
    pool = Pool(5)
    for i in range(30):
        pool.apply_async(func=foo, args=(i,))
    pool.close()  # 等子进程执行完后关闭进程池
    pool.join()
