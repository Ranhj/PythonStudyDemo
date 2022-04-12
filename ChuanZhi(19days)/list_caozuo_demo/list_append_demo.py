# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/5 10:13
# IDE:        PyCharm
# className:  list_append_demo.py

# 列表数据可改的 --列表可变类型
# append函数追加数据的时候如果数据是一个序列，追加整个序列到列表的结尾
name_list = ['Tom', 'Jack', 'Yang']
name_list.append('张三')          # ['Tom', 'Jack', 'Yang', '张三']
name_list.append([1, 2, 3])      # ['Tom', 'Jack', 'Yang', [1, 2, 3]]
print(name_list)