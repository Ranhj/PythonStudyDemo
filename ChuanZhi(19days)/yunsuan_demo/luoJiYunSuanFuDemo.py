# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/1 10:31
# a = 0
# b = 1
# c = 2
# # 1. and:   与：  都真才真
# print('-----------and-----------')
# print((a < b) and (c > b))
# print(a > b and c > b)
#
# # 2. or:    或：  一真则真，都假才假
# print('-----------or-----------')
# print(a < b or c > b)
# print(a > b or c > b)
# print(a > b or c < b)
#
# # 3. not:   非：  取反
# print('-----------not-----------')
# print(not False)
# print(not True)
# print(not c > a)


a = 0
b = 1
c = 2
# and运算符，只要有一个值为0，则结果为0，否则结果为最后一个非0数字
print(a and b)  # 0
print(b and a)  # 0
print(a and c)  # 0
print(c and a)  # 0
print(b and c)  # 2
print(c and b)  # 1
# or运算符，只有所有值为0结果才为0，否则结果为第一个非0数字
print(a or b)   # 1
print(a or c)   # 2
print(b or c)   # 1
