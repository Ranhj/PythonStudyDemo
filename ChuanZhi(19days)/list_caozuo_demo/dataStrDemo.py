# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/3 11:15
# 单引号及双引号字符串手动换行操作后会自动加上一个'\'，且打印格式不会打印出换行
a = 'h' \
    'i'
print(a)
print(type(a))
b = "he" \
    "llo"
print(b)
print(type(b))

# 三个单引号及双引号，手动换行操作后，打印格式会按照手动调整的格式进行打印
c = '''Hello
W
  o
    r
      l
         d'''
print(c)
print(type(c))
d = """H
e
 l
  l
   o
     Python"""
print(d)
print(type(d))

# 如果打印的字符串里有单引号'，那么要么使用双引号，要么在使用单引号的时候在前面加转义字符'\'
e = "I'm RHJ"
print(e)
f = 'I\'m RHJ'
print(f)

