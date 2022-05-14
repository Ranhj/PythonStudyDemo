# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-13 11:04
# className:  shengchengqi_demo.py
# generator 生成器
# 生成器一共两种创建方式
# 1 (x*2 for x in range(5))

s = (x*2 for x in range(5))
# print(s)    # <generator object <genexpr> at 0x000002A5855434A0>
# print(s.__next__())
# print(next(s))  # 0      等价于s.__next__()  in Py2:s.next()
# print(next(s))  # 2
# print(next(s))  # 4
# print(next(s))  # 6
# print(next(s))  # 8
# print(next(s))  # StopIteration

# 生成器就是一个可迭代对象(Iterable)
# for i in s:
#     print(i)

# # 2.yield
# def foo():
#     print('ok')
#     yield 1
#
# g = foo()
# print(g)    # <generator object foo at 0x000002237BBF34A0>


# def fib(max):
#     n, before, after = 0, 0, 1
#     while n < max:
#         print(after)
#         before, after = after, before+after
#         n = n + 1
# fib(10)


def fib1(max):
    x, y, z = 0, 0, 1
    while x < max:
        print(z)
        y, z = z, y+z
        x = x + 1
fib1(10)