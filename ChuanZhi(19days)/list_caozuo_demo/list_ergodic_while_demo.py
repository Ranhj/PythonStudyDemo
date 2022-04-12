# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/5 15:02
# IDE:        PyCharm
# className:  list_ergodic_while_demo.py

# 遍历：依次按顺序访问到序列的每一个数据
name_list = ['Tom', 'Jack', 'Yang']
i = 0
while i < len(name_list):
# while i <= len(name_list) - 1:    # 也可以这样写
    print(name_list[i])
    i += 1