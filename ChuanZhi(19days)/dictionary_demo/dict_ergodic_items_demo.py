# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/7 15:07
# IDE:        PyCharm
# className:  dict_ergodic_items_demo.py
# 查找当前字典所有的键值对，返回一个可迭代的对象
dict1 = {'name': 'Tom', 'age': 18, 'gender': '男', 'hobby': 'guitar'}
for item in dict1.items():
    print(item)