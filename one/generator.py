from collections import Iterable,Iterator
L=[x*x for x in range(10)]#创建一个list
print(L)
g=(x*x for x in range(10)) #创建一个生成器
print(g)
# print(next(g))
for n in g:#generator也是可迭代对象
    print(n)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
fib(6)

#如果一个函数定义中包含关键字yield，那么这个就不是普通的函数，而是一个generator
def fibg(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'


fibg1 = fibg(6)
print(fibg1)
print(next(fibg1))
for n in fibg1:
    print(n)

def triangles():
    row=[1]
    while True:
        yield(row)
        row=[1]+[row[k]+row[k+1] for k in range(len(row)-1)]+[1]
print(triangles())

n=0
for result in triangles():
    print(result)
    n=n+1
    if n==10:
        break
#迭代器
L=['A','B','C','D']
print(isinstance(L,Iterable))
print(isinstance(L,Iterator))
print(isinstance(iter(L),Iterator))
i = iter(L)
while True:
    try:
        x=next(i)
        print(x)
    except StopIteration:
        break