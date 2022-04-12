# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 9:44
# IDE:        PyCharm
# className:  replaceDemo.py
# replace()
'''
    replace() 把are 换成 bbb ccc说明replace函数有返回值，返回值是修改后的字符串
    调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
    说明 字符串是不可变数据类型
        数据是否可以改变划分为： 可变类型 和 不可变类型
'''
str1 = 'Who are you ? What are you doing?'
mystr = str1.replace('are', 'bbb')      # Who bbb you ? What bbb you doing? 不写替换次数默认替换所有符合字串条件的
print(mystr)
print(str1.replace('are', 'ccc', 1))    # Who ccc you ? What are you doing? 写上 次数 则会按照次数来替换
print(str1.replace('are', 'ccc', 10))    # Who ccc you ? What are you doing? 如果超出次数 则会替换所有符合提交子串
print(str1)                             # Who are you ? What are you doing? replace()不会改变字符串

