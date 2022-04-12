# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 10:40
# IDE:        PyCharm
# className:  set_del_discard_demo.py

# discard() 删除指定数据，如果数据不存在不会报错（用remove()删除不存在的数据会报错）
s1 = {10, 20, 30}
s1.discard(10)
print(s1)           # {20, 30}
s1.discard(10)
print(s1)           # {20, 30}