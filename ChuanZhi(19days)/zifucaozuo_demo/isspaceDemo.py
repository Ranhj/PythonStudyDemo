# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 15:40
# IDE:        PyCharm
# className:  isspaceDemo.py

# isspace() 如果字符串中只包含空白，则返回True，否则返回False
mystr = 'aaa'
mystr2 = 'a   b'
mystr3 = 'a2'
mystr4 = '123'
mystr5 = '    '
print(mystr.isspace())       # False
print(mystr2.isspace())      # False
print(mystr3.isspace())      # False
print(mystr4.isspace())      # False
print(mystr5.isspace())      # True
