# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 16:13
# IDE:        PyCharm
# Title:      func_parameter_demo3.py
# 缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值
# 注意：所有位置参数必须出现在默认参数前，包括函数定义和调用
# 函数调用时，如果为缺省参数传值则修改默认参数值；否则使用这个默认值
def user_info(name, age, gender='男'):
    print(f'您的姓名是{name}, 年龄是{age}, 性别是{gender}')

user_info('Jack', 18)               # 您的姓名是Jack, 年龄是18, 性别是男
user_info('HanMeimei', 17, '女')     # 您的姓名是HanMeimei, 年龄是17, 性别是女