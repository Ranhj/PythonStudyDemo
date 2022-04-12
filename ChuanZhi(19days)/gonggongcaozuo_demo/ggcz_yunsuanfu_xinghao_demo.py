# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 15:40
# IDE:        PyCharm
# Title:  ggcz_yunsuanfu_xinghao_demo.py
# 公共操作 复制： *
str1 = 'A'
list1 = ['Hello']
t1 = ('Hi',)
# *：复制
print(str1 * 5)                     # AAAAA
print('-' * 10, '靠', '-' * 10)     # ---------- 靠 ----------
print(list1 * 5)                    # ['Hello', 'Hello', 'Hello', 'Hello', 'Hello']
print(t1 * 5)                       # ('Hi', 'Hi', 'Hi', 'Hi', 'Hi')

dict1 = {'name':'Jack'}     # 字典不支持复制操作
# print(dict1 * 2)            # 会报错：TypeError: unsupported operand type(s) for *: 'dict' and 'int'
