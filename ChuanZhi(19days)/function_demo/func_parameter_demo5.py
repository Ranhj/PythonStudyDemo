# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 16:42
# IDE:        PyCharm
# Title:      func_parameter_demo5.py
# 包裹关键字传递
def user_info(**kwargs):
    print(kwargs)
user_info()     # {}
user_info(name='Jack', age=20, gender='男')  # {'name': 'Jack', 'age': 20, 'gender': '男'}
