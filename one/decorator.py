a_string='this is a global variable'
def foo():
    a_string='test'
    print(locals())

foo()
print(a_string)

def outer():
    def inner():
        print('inside inner')
    return inner
fo=outer()
print(fo)
fo()

def outer1():
    x=1
    def inner1():
        print(x)
    return inner1
fo1=outer1()
print(fo1)
fo1()

#===============
def outer2(some_func):
    def inner2():
        print('before some func')
        ret=some_func()
        return ret+1
    return inner2
def foo2():
    return 1
decoratoed=outer2(foo2)
print(decoratoed())

#=======demo=========
def logger(func):
    def inner(*args,**kwargs):
        print('Arguments were : %s,%s'%(args,kwargs))
        return func(*args,**kwargs)
    return inner

@logger
def add(x,y=1):
    return x+y
@logger
def sub(x,y):
    return x-y
print(add(1,2))
print(sub(1,2))



