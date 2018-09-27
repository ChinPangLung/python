from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    # value的属性则是自动赋给成员的int常量，默认从1开始计数
    print(name,'=>',member,',',member.value)

@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Web=3
    Thu=4
    Fri=5
    Sat=6
day1=Weekday.Mon
print(day1)

@unique
class Gender(Enum):
    Male=0
    Female=1
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        if isinstance(gender,Gender):
            self.gender=gender
        else:
            raise ValueError('只接收枚举类型')

bart=Student('bart',Gender.Male)
if bart.gender==Gender.Male:
    print('success')
else:
    print('fail')

