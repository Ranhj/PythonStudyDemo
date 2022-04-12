# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 11:29
# IDE:        PyCharm
# className:  stripDemo.py

# lstrip()  删除字符串左侧的空白字符
mystr = '  abc  '
new_mystr = mystr.lstrip()
print(new_mystr)

# rstrip() 删除字符串右侧的空白字符
mystr2 = '  abc  '
new_mystr2 = mystr2.rstrip()
print(new_mystr2)

# strip() 删除字符串两侧的空白字符
mystr3 = '  a b c  '
new_mystr3 = mystr3.strip()
print(new_mystr3)