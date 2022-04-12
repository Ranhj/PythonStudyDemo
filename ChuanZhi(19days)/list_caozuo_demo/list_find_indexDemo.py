# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 17:11
# IDE:        PyCharm
# className:  list_find_indexDemo.py

name_list = ['Tom', 'Jack', 'Yang']
print(name_list)        # ['Tom', 'Jack', 'Yang']
print(name_list[0])     # Tom
print(name_list[1])     # Jack
print(name_list[2])     # Yang

# index() 返回指定数据所在位置的下标，如果没查到则报错
print(name_list.index('Jack'))      # 1  返回Jack的索引值：1
print(name_list.index('Jacks'))     # 查找不到报错：ValueError: 'Jacks' is not in list
