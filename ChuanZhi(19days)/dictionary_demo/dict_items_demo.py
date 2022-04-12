# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/7 14:15
# IDE:        PyCharm
# className:  dict_items_demo.py

# items()   查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是字典的key，元组数据2是字典key对应的值
dict1 = {'name': 'Tom', 'age': 18, 'gender': '男', 'hobby': 'guitar'}
print(dict1.items())
