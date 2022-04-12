# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/7 13:38
# IDE:        PyCharm
# className:  del_dict_demo.py

dict1 = {'name': 'Tom', 'age': 18, 'gender': '男', 'hobby': 'guitar'}
# del dict1               # 写法一 del 字典名：删除成功  NameError: name 'dict1' is not defined
# del(dict1)              # 写法二 del(字典名)：删除成功  NameError: name 'dict1' is not defined
# del dict1['name']       # 删除指定键值对 删除成功  {'age': 18, 'gender': '男', 'hobby': 'guitar'}
# del dict1['names']      # 删除不存在的键值对 报错  KeyError: 'names'
print(dict1)