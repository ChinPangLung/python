import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
result = move(100, 100, 60, math.pi / 6)
print(result)
#python 的函数返回多个值其实就是返回一个tuple
#位置参数
def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
#默认参数
def power2(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*n
    return s
#可变参数
def calc(number):
    sum=0
    for n in number:
        sum=sum+n
    return  sum
print(calc((1,2,3,4)))
#===>
def calc1(*number):
    sum =0
    for n in number:
        sum=sum+n
    return  sum
print(calc1(1,2,3,4))
tuple=(1,2,3,4,5)
print(calc1(*tuple))#list tuple前面加个*变成可变参数传进去
#关键字参数
def person(name,age,**kwargs):
    print(name,age,'other:',kwargs)
person('lzp',27)
person('lung',26,city='guangzhou',sex='F')
extra={'city':'bj','sex':'L'}
person('lzp',30,**extra)#dict前面加**变成关键字参数传入
#命名关键字，只接收命名的关键字参数。
def person2(name,age,*,city,job):
    print(name,age,city,job)
person2('l',23,city='zhaoqing',job='IT')
# person2('ll',24,'gz','it') #这是错误的，命名关键字必须加上参数名

