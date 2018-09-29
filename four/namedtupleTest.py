from collections import namedtuple

Point = namedtuple('Ponit', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
print(p.y)

Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque

d = deque(['a', 'b', 'c'])
d.append('x')
d.appendleft('y')
print(d)
d.pop()
print(d)
d.popleft()
print(d)

# defaultdict
from collections import defaultdict

defaultdict1 = defaultdict(lambda: 'N/A')
defaultdict1['key'] = 'bac'
print(defaultdict1['key'])
print(defaultdict1['key1'])

# orderedDict 因为dict的可以是无序的，要保证key的顺序，可以用orderedDict
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)
print(od)

# Counter是一个简单的计数器
from collections import Counter

counter = Counter()
for c in 'programming':
    counter[c] = counter[c] + 1

print(counter)
