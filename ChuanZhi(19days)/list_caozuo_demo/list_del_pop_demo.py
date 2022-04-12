# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/5 10:52
# IDE:        PyCharm
# className:  list_del_pop_demo.py

# pop() 删除指定下标的数据，如果不指定下标，默认删除最后一个数据，无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据
name_list3 = ['Tom', 'Jack', 'Yang']
del_name_list3 = name_list3.pop()
print(del_name_list3)           # Yang    默认删除并返回最后一个数据
print(name_list3)               # ['Tom', 'Jack']

name_list4 = ['Tom', 'Jack', 'Yang']
del_name_list4 = name_list4.pop(0)  # 指定下标进行删除
print(del_name_list4)               # Tom   返回指定删除的数据
print(name_list4)                   # ['Jack', 'Yang']