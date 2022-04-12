# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 16:28
# IDE:        PyCharm
# Title:      func_parameter_demo4.py
"""
不定长参数也叫可变参数
用于不确定调用的时候会传递多少个参数（不传参也可以）的场景
此时，可用包裹（packing）位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便

注意：传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组（tuple）
args是元组类型，这就是包裹位置传递
"""
def user_info(*args):
    print(args)

user_info('Tom',)               # ('Tom',)
user_info('Jack', 20)           # ('Jack', 20)
user_info('Lily', 18, '女')     # ('Lily', 18, '女')
user_info()                     # ()