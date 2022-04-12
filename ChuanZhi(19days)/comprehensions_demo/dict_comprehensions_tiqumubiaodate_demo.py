# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/10 10:36
# IDE:        PyCharm
# Title:      dict_comprehensions_tiqumubiaodate_demo.py
# 提取字典中目标数据
# 需求： 提取电脑台数大于等于200
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
print(counts.items())   # 用 字典名.items() 迭代器获取所有数据  dict_items([('MBP', 268), ('HP', 125), ('DELL', 201), ('Lenovo', 199), ('acer', 99)])
# 获取所有键值对数据，判断value值大于等于200， 返回  字典
dict1 = {key: value for key, value in counts.items() if value >= 200}
print(dict1)            # {'MBP': 268, 'DELL': 201}
