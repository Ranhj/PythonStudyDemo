# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 10:16
# IDE:        PyCharm
# className:  list_split_demo.py
# split() 分割，返回一个列表，丢失分割字符（用哪个字符去分割，就会丢失哪个字符）
list1 = 'you and me and she or he'
print(list1.split('and'))        # ['you ', ' me ', ' she or he']
print(list1.split('and', 1))     # ['you ', ' me and she or he']
print(list1.split('and', 10))    # ['you ', ' me ', ' she or he']