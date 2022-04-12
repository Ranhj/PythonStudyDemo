# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 14:56
# IDE:        PyCharm
# className:  startSwith_endSwithDemo.py

mystr = 'goodluck for you'
# startswith( 字串， 开始位置下标， 结束位置下标 )判断字符串是否由某个子串开头
print(mystr.startswith('good'))     # True
print(mystr.startswith('GOOD'))     # False 区分大小写
print(mystr.startswith('go', 0, 3)) # True

# endswith( 字串， 开始位置下标， 结束位置下标 )判断字符串是否由某个子串结尾
print(mystr.endswith('you'))        # True
print(mystr.endswith('YOU'))        # False 区分大小写
print(mystr.endswith('you', 0, 3))  # False