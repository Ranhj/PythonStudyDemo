# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/2/28 15:30
# 1.float() 将数据转换成浮点型
num1 = 1
print(float(num1))
print(type(float(num1)))
str1 = '18'
print(float(str1))
print(type(float(str1)))

# 2.str() 将数据转换成字符串型
num2 = 2
print(str(num2))
print(type(str(num2)))

# 3.tuple() 将一个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))

# 4.list() 将一个序列转换成列表
tuple1 = (1, 2, 3)
print(list(tuple1))
print(type(list(tuple1)))

# 5.eval() 计算在字符串 串中的有效python表达式，并返回一个对象
print('-------eval():其实就是转换成数据原本的类型--------')
str2 = '1'
str3 = '1.0'
str4 = '[100, 200, 300]'
str5 = '(1000, 2000, 3000)'
print(eval(str2))
print(type(eval(str2)))
print(eval(str3))
print(type(eval(str3)))
print(eval(str4))
print(type(eval(str4)))
print(eval(str5))
print(type(eval(str5)))
