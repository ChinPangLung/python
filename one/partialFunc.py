import functools
print(int('12345'))
print(int('12345',base=8))
print(int('12345',base=16))

def int2(x,base=2):
    return int(x,base)
print(int2('1000000'))
print(int2('1000001'))
#functools.partoal偏函数就是帮助我们处理创建int2这种问题的
# 简单来说，偏函数就是把一个函数的某些参数给固定住（就是设置函数入参的默认值），返回一个新的函数，调用这个函数会变得更加简单
int3=functools.partial(int,base=2)
print(int3('1000000'))
print(int3('1010101'))
print(int3('1010101',base=8))

max=functools.partial(max,10)
print(max(1,5,6,9))
