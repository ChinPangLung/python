def my_range(max_number):
    sequence = []
    index = 0
    while index < max_number:
        sequence.append(index)
        index += 1
    return sequence


l = my_range(10)
print(l)


# 上边的创建list区间小没有问题，但是如果创建一个1亿个长度的列表，内存肯定不够的，这个时候需要用生成器来创建

def lazy_range(Max_number):
    index = 0
    while index < Max_number:
        yield index
        index += 1


g = lazy_range(10000000000000000)
print(g)

for x in range(10):
    print(next(g))

#生成器其实是协程的雏形了
