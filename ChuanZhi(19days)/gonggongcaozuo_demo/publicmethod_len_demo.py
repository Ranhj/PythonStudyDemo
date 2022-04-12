# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 17:08
# IDE:        PyCharm
# Title:      publicmethod_len_demo.py

# 公共方法 len() 计算容器中元素个数
str1 = 'abcdef'
list1 = [1, 2, 3, 4, 5]
t1 = (10, 20, 30, 40, 50)
s1 = {100, 200, 300, 400, 500}
dict1 = {'name': 'Tom', 'hobby': 'guitar'}
print(len(str1))    # 6
print(len(list1))   # 5
print(len(t1))      # 5
print(len(s1))      # 5
print(len(dict1))   # 2  字典dict1里有两个键值对，所以显示 2