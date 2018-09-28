#第一种方式就是利用print打印输出日志
def foo(s):
    n=int(s)
    print('>>> n=%d'% n)
    return 10/n
def main():
    foo(1)
main()

#断言
def foo1(s):
    n=int(s)
    assert n!=0,'n is zero'
    return 10/n
def main1():
    foo1('1')
main1()

#logging
import logging
logging.basicConfig(level=logging.INFO)#logging允许指定记录信息的级别有debug、info、waring、error
s='0'
n2=int(s)
logging.info('n=%d'% n2)
print(10/n2)

#pycharm 断点