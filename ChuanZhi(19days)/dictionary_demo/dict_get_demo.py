# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/7 13:57
# IDE:        PyCharm
# className:  dict_get_demo.py

# 语法：   字典序列.get(key, 默认值)
# 如果当前查找的key不存在则返回第二个参数（默认值），如果省略第二个参数，则返回None
dict1 = {'name': 'Tom', 'age': 18, 'gender': '男', 'hobby': 'guitar'}
print(dict1.get('name'))        # Tom
print(dict1.get('id', 100))     # 100
print(dict1.get('id'))          # None
