from functools import reduce
#map和reduce是python内建函数
#map函数接收两个参数，一个是函数，一个是Iterable迭代对象.map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(r)
r = list(r)
print(r)
str=map(str,[1,2,3,4,5,6,7,8,9])
print(list(str))

#reduce函数把一个函数作用在一个序列，这个函数必须接收两个参数，reduce把结果和序列下一个函数元素做累积计算
def add(x,y):
    return x+y
sum = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sum)
def fn(x,y):
    return x*10+y

fn = reduce(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(fn)