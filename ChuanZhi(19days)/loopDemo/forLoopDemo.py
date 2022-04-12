# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/2 17:09
print('----------continue----------')
str1 = 'Hello Python'
for i in str1:
    if i == 'o':
        print('遇到o不打印')
        continue
    print(i)
print('----------break----------')
str2 = 'Hello Python'
for i in str2:
    if i == 'o':
        print('遇到o不打印，直接退出整个循环')
        break
    print(i)