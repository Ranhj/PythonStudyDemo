# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/2 9:49
'''
三目运算符语法：
    条件成立执行的表达式 if 条件 else 提交不成立执行的表达式
'''
a = 1
b = 2
c = a if a > b else b
print(c)

aa = 10
bb = 20
cc = print('aa比bb大') if aa > bb else print('bb比aa大')


# 需求：有两个变量，比较大小，如果变量1大于变量2 执行 变量1 - 变量2； 否则执行 变量2 - 变量1
num = 5
num2 = 20
num3 = num - num2 if num > num2 else num2 - num
print(num3)

