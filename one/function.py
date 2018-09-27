#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(abs(100))
print(abs(-20))
print(max(1, 2, 3))
print(max(-1, -5, 9, 4))
# 数据类型转换
print(int('234'))
print(int(12.34))
print(float(12))
print(str(123))
print(bool(1))
print(bool(''))
# 函数可以赋值给一个变量
a = abs
print(a(-1))
print(hex(25))
print(hex(255))

# 定义函数 def
def my_abs(X):
    if not isinstance(X,(int,float)):
        raise TypeError('bad operand type')
    if X >= 0:
        return X
    else:
        return -X
i = my_abs(-199)
print(i)

#空函数
def nop():
    pass
nop()

