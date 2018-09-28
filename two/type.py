#type()函数是可以查看一个类型或者变量的类型
class Hello(object):
    def hello(self,name):
        print('hello : %s' % name)
h=Hello()
h.hello('long')
print(type(Hello))
print(type(h))

#type()函数还可以创建新的类
def fn(self,name='world'):
    print('hello,%s'% name)
Hello1=type('Hello1',(object,),dict(hello=fn))#创建Hello1的类
h1=Hello1()
h1.hello()
print(type(Hello1))
print(type(h1))

#metaclass元类 先定义元类，可以创建类，最后创建实例。==》其实就是可以看成类是metaclass创建的实例
class ListMetaclass(type):
    def __new__(cls, name, bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class myList(list,metaclass=ListMetaclass):
    pass
l=myList()
l.add(1)
print(l)
