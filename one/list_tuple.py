#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print ('hello world')
# name=input("请输入你的名字:")
# print(name)
s1=72
s2=85
# list 列表
classmates=['lzp','cwy','zyy']
print(classmates)
i = len(classmates)
print(i)
print(classmates[0])
print(classmates[-1])
classmates.append('yyx')
print(len(classmates))
classmates.insert(1,'xjj')
print(classmates[1])
classmates.pop()
print(classmates)
classmates[1]='lungzp'
print(classmates)
classmates.append(11)
classmates.append(11)
print(classmates)
classmates.append(['111',98])
print(classmates)
# 元祖 tuple 不可变化，比list安全。所谓的不变时指向不变
tuple=(11,11,22,34)
print(tuple)
print(tuple[0])
print(tuple[-1])
tuple1=(1,)
print(tuple1)
# 可变的tuple
t=('a','b',['A','B'])
print(t)
t[2][0]='X'
t[2][1]='Y'
print(t)
# test
L=[
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])