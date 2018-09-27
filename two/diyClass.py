class Student(object):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return 'Student object (name:%s)'% self.name

student = Student('Lung')

print(student)

#__iter__定制类返回一个可迭代对象
class fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10000:
            raise StopIteration()
        return self.a
    def __getitem__(self, item):
        a,b=1,1
        for x in range(item):
            a,b=b,a+b
        return a


for n in fib():
    print(n)

f=fib()
print(f[0])
print(f[1])
print(f[2])
print(f[10])

class Student1(object):
    def __init__(self):
        self.name='lung'
    def __getattr__(self, item):
        if item=='score':
            return 99

s1=Student1()
print(s1.name)
# print(s1.score) #不存在会报错 使用__getattr__()解决
print(s1.score)

#__call__
class Student2(object):
    def __init__(self,name):
        self.name=name
    def __call__(self, *args, **kwargs):
        print('my name is %s '% self.name)
s2=Student2('chinLung')
s2()

