#高阶函数，说白了就是一个函数可以接收另一个函数作为入参
def add(x,y,f):
    print(f(x)+f(y))
    return f(x)+f(y)
add(5,-6,abs)
#返回函数 函数作为返回值
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=lazy_sum(1,2,3,4,5,6)
f1=lazy_sum(1,2,3,4,5,6,7)
print(f)
print(f())
print(f1())