# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 15:37
# IDE:        PyCharm
# className:  isalnumDemo.py

# isalnum() 如果字符串至少有一个字符并且所有字符都是字母或数字或字母及数字的组合则返回True，否则返回False
mystr = 'aaa'
mystr2 = 'a b'
mystr3 = 'a2'
mystr4 = '123'
print(mystr.isalnum())       # True
print(mystr2.isalnum())      # False
print(mystr3.isalnum())      # True
print(mystr4.isalnum())      # True