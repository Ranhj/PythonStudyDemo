# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/9 10:51
# IDE:        PyCharm
# Title:      ggcz_rongqitypechange_list_demo.py

# list(): 转换成列表
s1 = {200, 100, 300, 500, 400}
t1 = ('a', 'b', 'c', 'd', 'e')
# set --> list:
list1 = list(s1)
print(type(list1))      # <class 'list'>
print(list1)            # [100, 200, 300, 400, 500]
# tuple --> list:
list2 = list(t1)
print(type(list2))      # <class 'list'>
print(list2)            # ['a', 'b', 'c', 'd', 'e']
