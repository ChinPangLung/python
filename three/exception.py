# 所有的类型错误都继承BaseException
try:
    print('try..')
    r = 10 / int('0')
    print('result....', r)
except ZeroDivisionError as e:
    print('ecception', e)
except ValueError as e:
    print('valueError', e)
else:
    print('no error')
finally:
    print('finally...')
print('END')


# error.py
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('1')


main()

# logging模块记录错误信息
# err_logging.py
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('1')
    except Exception as e:
        logging.exception(e)


main()
print('END')


# raise 抛出错误 err_raise.py

def foo(s):
    n = int(s)
    if n == 0:
        raise BaseException('invalid value:%s' % s)
    return 10 / 0


foo('0')
