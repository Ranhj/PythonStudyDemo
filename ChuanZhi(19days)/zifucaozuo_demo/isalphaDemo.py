# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 15:29
# IDE:        PyCharm
# className:  isalphaDemo.py

# isalpha() 如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False
mystr = 'aaa'
mystr2 = 'a b'
mystr3 = 'a2'
mystr4 = '123'
print(mystr.isalpha())      # True  都是字符，所以返回True
print(mystr2.isalpha())     # False 字符串包含空格，所以返回False
print(mystr3.isalpha())     # False 字符串包含数字，所以返回False
print(mystr4.isalpha())     # False 字符串都是数字，所以返回False
