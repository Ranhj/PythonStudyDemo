# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-11 16:37
# className:  decrator_demo.py
# decorator?
import time
start = time.time()
time.sleep(1)
end = time.time()
print(end - start)
print(start)
print(end)

# 遵守开放封闭原则
def foo():
    start = time.time()
    print('foo......')
    time.sleep(2)
    end = time.time()
    print('spend: %s' % (end - start))

def bar():
    start = time.time()
    print('bar:')
    time.sleep(5)
    end = time.time()
    print('spend:%s' % (end - start))

def show_time(f):
    start = time.time()
    f()
    end = time.time()
    print('spend: %s' % (end - start))

# show_time(foo)
# show_time(bar)



def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('spend: %s' % (end - start))
    return inner()

# foo = show_time(foo)
# foo()
# f2 = show_time(f2)
# f2()



def show_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend: %s' % (end_time - start_time))
    return wrapper
@show_time  # foo=show_time(foo)
def foo():
    print('hello foo')
    time.sleep(3)
foo()



def show_time(f):
    def inner(x, y):
        start_time = time.time()
        f(x, y)
        end_time = time.time()
        print('spend: %s' % (end_time - start_time))
    return inner
@ show_time
def add(a, b):
    print(a + b)
    time.sleep(1)
add(1, 5)



def show_time(f):
    def inner(*x, **y):
        start_time = time.time()
        f(*x, **y)
        end_time = time.time()
        print('spend: %s' % (end_time - start_time))
    return inner
@ show_time
def add2(*a, **b):
    sum=0
    for i in a:
        sum+=i
    print(sum)
    time.sleep(1)
add2(1, 5, 6, 8)


# 功能函数加参数
def logger(flag=''):
    def show_time(f):
        def inner(*x, **y):
            start = time.time()
            f(*x, **y)
            end = time.time()
            print('spend: %s' % (end - start))
            if flag == 'true':
                print('日志记录')

            return inner
    return show_time

@logger('true') # @show_time

def add(*a, **b):
    sums = 0
    for i in a:
        sum += i
        print(sum)
        time.sleep(1)
add(1, 2, 3, 4, 5, 6)

@logger('true')
def bar():
    print('bar......')
    time.sleep(2)
bar()

