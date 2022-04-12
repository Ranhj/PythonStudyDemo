# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/9 14:21
# IDE:        PyCharm
# Title:      list_comprehensions_demo.py
# 列表推导式 作用：用一个表达式创建一个有规律的列表或控制一个有规律列表   列表推导式又叫列表生成式
# 需求：创建一个0，1，2，3...10的列表
# 1.循环实现；
'''
1.1 创建空列表
1.2 循环将有规律的数据写入到列表
'''
# while循环实现
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# for循环实现
list2 = []
for i in range(10):
    list2.append(i)
    i += 1
print(list2)

# 2.列表推导式（化简代码：创建或控制有规律的列表）
list3 = [i for i in range(10)]  # for 左侧的 i 是返回值
print(list3)