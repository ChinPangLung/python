#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a test module' #模块的文档注释

__author__='lungzp' #使用__author__变量把作者写进去

import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello, %s!' % args[1])
    else:
        print('Too many arguments')

if __name__=='__main__':
    test()

#作用域
#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊的用途，我们自己的变量一般不要使用这种变量名
#类似_xxx和__xxx这样的函数或者变量是非公开的(private)，不应该被直接引用。比如：_abc,__abc
def _private_1(name):
    return 'Hello,%s' % name
def _private_2(name):
      return 'Hi, %s' % name
def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
print(greeting('zp'))