# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/7 11:30
# IDE:        PyCharm
# className:  update_dict_demo.py
# 写法： 字典序列[key] = 值
# 如果key存在则修改这个key对应的值；如果key不存在则新增此键值对
dict1 = {'name': 'Tom', 'age': 18, 'gender': '男', 'hobby': 'guitar'}
print(dict1)            # {'name': 'Tom', 'age': 18, 'gender': '男', 'hobby': 'guitar'}
dict1['name'] = 'Jame'
print(dict1)            # {'name': 'Jame', 'age': 18, 'gender': '男', 'hobby': 'guitar'}
dict1['id'] = 1001
print(dict1)            # {'name': 'Jame', 'age': 18, 'gender': '男', 'hobby': 'guitar', 'id': 1001}

