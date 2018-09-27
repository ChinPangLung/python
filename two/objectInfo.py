import types
#使用type可以查询对象的类型
print(type(123))
print(type('123'))
print(type(None))
a=abs
print(a(-1))
print(type(a))

#判断一个对象是否是函数，可以用types模块中定义的常量
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)

#使用dir()获取对象的所有属性和方法
print(dir('ABC'))

#实例属性和类属性
class Student(object):
    name='student'

s=Student()
print(s.name)
print(Student.name)
s.name='lzp'
print(s.name)
print(Student.name)
del s.name
print(s.name)