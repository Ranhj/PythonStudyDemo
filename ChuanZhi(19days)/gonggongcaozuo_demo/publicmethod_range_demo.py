# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/9 9:42
# IDE:        PyCharm
# Title:      publicmethod_range_demo.py
# range(start,end,step):生成从start到end的数字，步长为step，供for循环使用
# 如果不写开始，则默认从0开始；如果省略step，则默认步长为1
# range()生成的序列不包含end数字
print(range(1, 10, 1))  # range(1, 10) range必须要配合for循环才能拿到想要的数字，直接打印会直接显示range返回的可迭代对象

for i in range(1, 10):  # 循环遍历时，不包括结束位置，step步长省略则默认1
    print(i)    # 1 2 3 4 5 6 7 8 9
    i += 1

for i in range(10):
    print(i)    # 0 1 2 3 4 5 6 7 8 9
    i += 1

for i in range(1, 10, 2):
    print(i)    # 1 3 5 7 9
    i += 1

for i in range(0, 10, 2):
    print(i)    # 0 2 4 6 8
    i += 1

