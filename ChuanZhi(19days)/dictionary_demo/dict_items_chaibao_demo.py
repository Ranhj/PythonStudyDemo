# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/7 15:11
# IDE:        PyCharm
# className:  dict_items_chaibao_demo.py

# xx.items(): 返回可迭代对象，内部是元组，元组有2个数据
# 元组数据1是字典的key,元组数据2是字典的value
dict1 = {'name': 'Tom', 'age': 18, 'gender': '男', 'hobby': 'guitar'}
for key, value in dict1.items():
    # print(key)
    # print(value)
    # 目标：key = value
    print(f'{key}={value}')
