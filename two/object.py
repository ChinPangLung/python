#类和实例
class Student(object):
    #int方法的第一个参数永远是self，表示创建实例的本身
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s: %s ' % (self.name,self.score))
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'
bart=Student('long',98)
print(bart.name)
print(Student)
# bart.name='lungzp'
# print(bart.name)
bart.print_score()
print(bart.get_grade())

#访问限制
class Student1(object):
    # 类似java class的构造器
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s:=== %s' % (self.__name,self.__score))
    #类似java属性的get方法
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    #类似java属性的set方法
    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        self.__score=score

bart1=Student1('long',90)
bart1.print_score()
bart1.set_name('chinpang')
bart1.set_score(89)
print(bart1.get_name())
print(bart1.get_score())
#双下划线表示private，但是并不代表一定不能从外部访问，不能直接访问是因为python解释器把__name变量变成了_Student1__name,
# 所以我们还是可以通过_Student1__name来访问__name
print(bart1._Student1__name)
