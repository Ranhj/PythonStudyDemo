# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 10:39
# IDE:        PyCharm
# className:  set_del_remove_demo.py

# remove() 删除指定数据，如果数据不存在则报错（用discard()删除不存在的数据不会报错）
s1 = {10, 20, 30}
s1.remove(10)
print(s1)           # 成功删除 {20, 30}
# s1.remove(10)
# print(s1)       # 再次删除会报错：KeyError: 10
s2 = {10, 20}

s2.remove(10, 20)   # 全部删除会报错：TypeError: remove() takes exactly one argument (2 given)
print(s1)