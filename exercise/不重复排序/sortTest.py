#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午3:49
# @Author  : ChinPangLung
# @Site    : 
# @File    : sortTest.py
# @Software: PyCharm

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def main_test():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (i != k) and (j != k):
                    print(i, j, k)

if __name__ == '__main__':
    main_test()