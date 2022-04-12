# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/5 10:40
# IDE:        PyCharm
# className:  list_del_demo.py

# 删除列表 del ; del()
name_list = ['Tom', 'Jack', 'Yang']
del name_list         # NameError: name 'name_list' is not defined 已成功删除
del (name_list)       # NameError: name 'name_list' is not defined 已成功删除
print(name_list)

# del (list[])  可以删除指定下标的数据
name_list2 = ['Tom', 'Jack', 'Yang']
del name_list2[0]        # ['Jack', 'Yang']   指定删除第一个数据
print(name_list2)
