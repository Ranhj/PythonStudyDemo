# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/16 10:15
# IDE:        PyCharm
# Title:      buildinhigherorderfunc_map_demo.py
# 内置高阶函数  map(func, lst) 将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表(Python2)/迭代器(Python3)返回
# 1.准备列表数据
list1 = [1, 2, 3, 4, 5, 6]

# 准备2次方计算的函数
def func(x):
    return x ** 2

# 3.调用map函数
result = map(func, list1)

# 4.验收成功
print(result)            # <map object at 0x01A8B028>
print(list(result))      # 注意：这里将迭代器转换为列表是用"list"而非定义的列表名"list1"！！！[1, 4, 9, 16, 25, 36]
