# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 15:33
# IDE:        PyCharm
# className:  isdigitDemo.py

# isdigit() 如果字符串只包含数字则返回True否则返回False
mystr = 'aaa'
mystr2 = 'a b'
mystr3 = 'a2'
mystr4 = '123'
print(mystr.isdigit())          # False
print(mystr2.isdigit())         # False
print(mystr3.isdigit())         # False
print(mystr4.isdigit())         # True
