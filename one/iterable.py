import os
for ch in 'ABC':
    print(ch)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 列表生成式
list = [x * x for x in range(1, 11)]

print(list)

list1 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list1)

list2=[m+n for m in 'ABC' for n in 'XYZ']
print(list2)

list3=[d for d in os.listdir('.')]
print(list3)

L=['Hello','World','IBM','Apple']
list4=[s.lower() for s in L]
print(list4)
L1=['Hello','World','IBM','Apple',18]
list5=[s.lower() for s in L1 if isinstance(s,str)]
print(list5)