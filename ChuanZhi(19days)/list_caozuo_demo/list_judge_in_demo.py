# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 17:28
# IDE:        PyCharm
# className:  list_judge_in_demo.py

# 1.in 判断指定数据在某个列表序列，如果在返回True，否则返回False
name_list = ['Tom', 'Jack', 'Yang']
print('Tom' in name_list)       # True
print('Toms' in name_list)      # False

# 2. not in 判断指定数据不在某个列表序列，如果不在返回True，否则返回False
print('Tom' not in name_list)   # False
print('Toms' not in name_list)  # True
