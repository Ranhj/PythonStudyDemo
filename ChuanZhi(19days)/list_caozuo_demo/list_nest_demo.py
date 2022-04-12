# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/5 15:17
# IDE:        PyCharm
# className:  list_nest_demo.py

# 所谓列表嵌套指的就是一个列表里面包含了其他的子列表
name_list = [['张三', '李四', '王五'], ['Jack', 'Jame'], ['HanMeimei', 'Lily']]
print(name_list)            # [['张三', '李四', '王五'], ['Jack', 'Jame'], ['HanMeimei', 'Lily']]
print(name_list[1])         # ['Jack', 'Jame']
print(name_list[2][0])      # HanMeimei
print(name_list[2][0][0])   # H
print(name_list[2][0][1])   # a
print(name_list[2][0][2])   # n
