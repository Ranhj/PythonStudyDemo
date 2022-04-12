# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/16 9:24
# IDE:        PyCharm
# Title:      higherorderfunction_demo.py
# abs() 绝对值
print(abs(-11))     # 11

# round() 四舍五入
print(round(3.1))   # 3
print(round(3.5))   # 4
print(round(3.1415, 2))     # 3.14  round(x, y) y可以设置保留小数点后的位数

# 需求： 任意两个数字，按照指定要求整理数字(绝对值或四舍五入)后再进行求和计算
# 方法一：  绝对值
def add_num(a, b):
    return abs(a) + abs(b)
result = add_num(-10, 20)
print(result)   # 30

# 方法二：  高阶函数： f是第三个参数，用来接收将来传入的函数
def sum_num(a, b, f):
    return f(a) + f(b)

result2 = sum_num(2.2, -3, abs)     # 传入abs绝对值函数名，先求绝对值再求和
print(result2)      # 5.2

result3 = sum_num(3.5, 4.3, round)  # 传入round四舍五入函数名，先四舍五入再求和
print(result3)      # 8
