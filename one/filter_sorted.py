#filter也是接收一个函数和一个序列，和mao不同的是，filter把传入的函数依次作用于每个元素，然后根据True还是False决定保留还是不保留元素
def is_odd(n):
    return n%2==1

l = [1, 2, 3, 4, 5, 6, 7]
l1 = list((filter(is_odd,l)))
print(l1)

#sorted排序算法
list=[36,5,-12,9,-21]
print(sorted(list))
print(sorted(list,key=abs))
