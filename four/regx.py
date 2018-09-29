# \d表示匹配一个数字 \w表示匹配一个字母或者数字 \s表示空格 \s+表示至少一个空格
# .可以匹配任意字符 *表示任意个字符包括0个 +表示至少一个 ？表示0或者1个字符 {n}表示n个字符 {n,m}表示n-m个字符
# 进阶
# 要做更加精确的匹配 可以用[]表示范围
#   [0-9a-zA-Z\_]匹配任意一个数字，字母或者下划线
#   [0-9a-zA-Z\_]+可以匹配至少由一个数字，字母或者下划线组成的字符串 demo：‘a100’ ‘0_z’ 'Py0003'
#   [a-zA-Z\_][0-9a-zA-Z\_]{0,19}匹配限制变量的长度是1-20个字符，（前面1个字母加后面最多19个字符）
# A|B匹配A或者B 所以(P|p)ython可以匹配Python或者python
# ^表示行的开头 ^\d表示必须要以数字开头
# $表示行的结尾 \d$表示必须要以数字结尾
s = 'ABC\\-001'
print(s)
s1 = r'ABC\\-001'  # 使用r前缀，不用考虑转义的问题了
print(s1)

import re

# match()方法判断是否匹配，如果匹配成功返回一个match对象，否则返回一个None
match = re.match(r'^\d{3}\-\d{3,8}$', '010-123456')
print(match)
match1 = re.match(r'^\d{3}\-\d{3,8}$', '010-12')
print(match1)

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('faild')

# 分割字符
sp = 'a b  c'
print(sp.split(' '))
split = re.split(r'\s+', sp)
print(split)

sp1 = 'a,b c  d,f+g+j'
re_split = re.split(r'[\s+\,]+', sp1)
re_split1 = re.split(r'[\s\,]+', sp1)
print(re_split)
print(re_split1)

# 分组 用()表示的就是提取的分组 ^(\d{3})-(\d{3,8})$ 定义了两个分组 这样就直接可以提取区号和本地号码了
re_match = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
print(re_match)
print(re_match.group(0))  # 0表示永远都是原始字符串
print(re_match.group(1))
print(re_match.group(2))
# print(re_match.group(3)) #error
