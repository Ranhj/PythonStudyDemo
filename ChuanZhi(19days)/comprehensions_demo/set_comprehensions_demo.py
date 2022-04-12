# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/10 11:03
# IDE:        PyCharm
# Title:      set_comprehensions_demo.py
# 集合推导式
# 需求：创建一个集合，数据为下方列表的2次方
list1 = [1, 1, 2]
set1 = {i**2 for i in list1}
# 集合有自动去重功能，所以这个集合数据只有两个数据 1  4
print(set1)     # {1, 4}

