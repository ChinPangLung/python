#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# dict 字典==》map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
d['Bob'] = 90
print(d['Bob'])
print(d)
print('Lung' in d)
print('Bob' in d)
d.pop('Bob')
print(d)
# set 一组key的集合，不存储value
s = set([1, 2, 3])
print(s)
s1 = ({1, 1, 2, 2, 3, 4})
print(s1)
s.add(5)
print(s)
s.remove(5)
print(s)
print(s & s1)
print(s | s1)
