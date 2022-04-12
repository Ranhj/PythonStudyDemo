# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 10:30
# IDE:        PyCharm
# className:  set_update_demo.py
# update() 往集合里增加数据序列
s1 = {10, 20, 30}
s1.update([1, 2, 3])    # 增加的数据是序列
print(s1)               # {1, 2, 3, 10, 20, 30}
# s1.update(100)          # 增加单一int数据会报错
print(s1)               # TypeError: 'int' object is not iterable
s1.update('abc')        # 添加字符串没问题
print(s1)               # {1, 2, 3, 'a', 'b', 10, 20, 'c', 30}