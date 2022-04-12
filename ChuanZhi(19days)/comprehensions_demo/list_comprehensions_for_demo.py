# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/9 16:40
# IDE:        PyCharm
# Title:      list_comprehensions_for_demo.py

# 多for的列表推导式等同于for循环嵌套

# 需求：创建列表如下：[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list1 = []
for i in range(1,3):
    for j in range(3):
        # 列表里面追加元组：循环前准备一个空列表，然后这里追加元组数据到列表
        list1.append((i, j))
print(list1)    # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 多个for实现列表推导式
list2 = [(i, j)for i in range(1, 3) for j in range(3)]
print(list2)    # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
