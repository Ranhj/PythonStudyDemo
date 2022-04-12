# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 15:57
# IDE:        PyCharm
# Title:      ggcz_yunsuanfu_in_notin_demo.py
# 公共操作 判断数据是否存在 ：in（在）   not in（不在）
str1 = 'abcd'
list1 = [10, 20, 30]
t1 = (100, 200, 300)
dict1 = {'name': 'Tom', 'hobby': 'guitar'}

# 1.判断字符a是否存在str1字符串里
print('-'* 10, '用in / not in判断字符串', '-'* 10)
print('a' in str1)              # True
print('a' not in str1)          # False
# 2.判断数据10是否存在列表list1里
print('-'* 10, '用in / not in判断列表', '-'* 10)
print(10 in list1)              # True
print(10 not in list1)          # False
# 3.判断100是否存在t1元组里
print('-'* 10, '用in / not in判断元组', '-'* 10)
print(100 in t1)                # True
print(100 not in t1)            # False
# 4.判断name是否存在dict1字典里
print('-'* 10, '用in / not in判断字典', '-'* 10)
print('name' in dict1)          # True
print('name' not in dict1)      # False
print('names' not in dict1)     # True
print('name' in dict1.keys())   # True
print('Tom' in dict1.values())  # True
