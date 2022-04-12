# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 17:13
# IDE:        PyCharm
# Title:      publicmethod_del_demo.py
# 公共方法  del 目标 或 del(目标)            删除
str1 = 'abcdef'
list1 = [1, 2, 3, 4, 5]
t1 = (10, 20, 30, 40, 50)
s1 = {100, 200, 300, 400, 500}
dict1 = {'name': 'Tom', 'hobby': 'guitar'}
# del str1
# print(str1)           # 删除成功
del(str1)
print(str1)           # 删除成功

# del list1               # 删除成功
# del(list1)              # 删除成功
# print(list1)
del list1[0]            # 指定删除下标0的数据
print(list1)            # 删除成功    [2, 3, 4, 5]

# del t1                      # 删除成功
# del(t1)                     # 删除成功
# print(t1)
del t1[1]                   # 针对元组下标进行删除操作失败
print(t1)                   # 报错：TypeError: 'tuple' object doesn't support item deletion

# del s1                          # 删除成功
del(s1)                         # 删除成功
print(s1)

# del dict1                          # 删除成功
# del(dict1)                         # 删除成功
# print(dict1)
del dict1['name']                    # 指定删除键值对key:name删除成功
print(dict1)                         # {'hobby': 'guitar'}