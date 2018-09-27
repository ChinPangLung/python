#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#if
age=3
if age>=18:
    print('your age is ',age)
    print('adult')
elif age>6:
    print('teenager')
else:
    print('kid') #判断条件只要是非零数值，非空字符串，非空list就判断为True，否则为False

# s=input("请输入年龄：")
# brith=int(s)
# if brith>=2000:
#     print('00后')
# else:
#     print('00前')

#for in
names=['lzp','cwy','zyy']
for name in names:
    print(name)
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)
print(list(range(5)))#range生成一个整数序列，list转成list
count=0
for y in range(101):
    count=count+y
print(count)
sum1=0
n =99
while n>0:
    sum1=sum1+n
    n=n-2
print(sum1)
#test
L=['Bart','Lisa','Adam']
for a in L:
    print('hello,'+a)