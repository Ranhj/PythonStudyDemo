# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/9 15:13
# IDE:        PyCharm
# Title:      list_comprehensions_if_demo.py
# 需求：创建0-10的偶数列表
# 方法一：range() 步长实现
list1 = [i for i in range(0, 10, 2)]
print(list1)

# 方法二：for循环加if 创建有规律的列表
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)
print(list2)

# 方法三：for循环配合if实现，改写成带if的列表推导式
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)
