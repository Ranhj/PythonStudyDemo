# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/10 9:20
# IDE:        PyCharm
# Title:      dict_comprehensions_creat_demo.py
# 需求：创建一个字典，字典key是1~5数字，value是这个数字的2次方
dict1 = {key: key**2 for key in range(1, 6)}    # value：key的2次方
print(dict1)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
