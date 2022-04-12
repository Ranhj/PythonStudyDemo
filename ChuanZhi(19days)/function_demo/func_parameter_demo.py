# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 15:23
# IDE:        PyCharm
# Title:      func_parameter_demo.py
# 位置参数：调用函数时根据函数定义的参数位置来传递参数
# 注意： 传递和定义参数的顺序及个数必须一致
def user_info(name, age, gender):
    print(f'您的名字是{name},年龄是{age}岁，性别是{gender}')

# user_info('Jack', '男')    # 少传一个参数，报错：TypeError: user_info() missing 1 required positional argument: 'gender'
# user_info('Jack', '男', 18)  # 位置错乱 ： 您的名字是Jack,年龄是男岁，性别是18
user_info('Jack', 18, '男')      # 您的名字是Jack,年龄是18岁，性别是男
