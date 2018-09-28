import pickle

d = dict(name='Bob', age=20, score=90)
dumps = pickle.dumps(d)
print(dumps)  # dumps表示把任意对象序列化成bytes
print(type(dumps))
# 序列化过程
fwb = open('dump.txt', 'wb')
pickle.dump(d, fwb)
fwb.close()

# 反序列化
with open('dump.txt', 'rb') as frb:
    loads = pickle.load(frb)
    print(loads)

print('=================')
# json
import json

json_dumps = json.dumps(d)
print(json_dumps)
print(type(json_dumps))
load = json.loads(json_dumps)
print(load)
print(type(load))

#json序列化实例对象
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
s=Student('Bob',20,99)
# print(json.dumps(s)) 不能这样序列化
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
dumps1 = json.dumps(s, default=student2dict)
print(dumps1)
#或者这样做
dumps2 = json.dumps(s, default=lambda obj: obj.__dict__)#把任意class实例变为dict
print(dumps2)
print(type(dumps2))

#json反序列化
def dict2Student(d):
    return Student(d['name'],d['age'],d['score'])


json_loads = json.loads(dumps2, object_hook=dict2Student)
print(json_loads)
print(json_loads.name)