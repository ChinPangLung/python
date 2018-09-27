# __slots__
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'lung'  # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 动态给实例绑定一个方法
s.set_age(25)
print(s.age)


def set_score(self, score):
    self.score = score


Student.set_score = set_score  # 为了给所有实例绑定方法，就是在class绑定方法

s1 = Student()
s1.set_score(100)
print(s1.score)


# 使用__slots__限制实例的属性
class Student1(object):
    __slots__ = ('name', 'age')  # 使用tuple定义允许绑定的属性名称


s2 = Student1()
s.name = 'longzpp'
print(s.name)
s2.age = 27
print(s2.age)


# s2.score=100 #报错了
# print(score)
class StudentExtendStud(Student1):  # __slots__定义只对当前的实例起作用，对继承的子类是不起作用的
    pass


g = StudentExtendStud()
g.score = 100
print(g.score)


# @property
class Student3(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('socre must between 0~100')
        self._score = value


s3 = Student3()
s3.set_score(60)
print(s3.get_score())


# s3.set_score(99999)
# print(s3.get_score())

class Student4(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('socre must between 0~100')
        self._score = value


s4 = Student4()
s4.score = 67
print(s4.score)

# s4.score=999
