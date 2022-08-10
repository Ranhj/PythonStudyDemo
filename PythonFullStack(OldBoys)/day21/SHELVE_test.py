# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-08-10 16:59
# className:  SHELVE_test.py
import shelve
# 先存， 存入了三种格式
f = shelve.open('SHELVE_text')
# f['info'] = {'name': 'alex', 'age': '18'}
# f['shopping'] = {'name': 'aaa', 'price': '123'}

# 再取， 不管存入的是哪种方式，以什么方式存的，就什么方式取
f = shelve.open('SHELVE_text')

# data = f.get('info')
data = f.get('shopping')    # {'name': 'aaa', 'price': '123'}
print(data)  # {'name': 'alex', 'age': '18'}



#  穿插
# d = {'name': 'alex', 'age': '18'}
# # d['name'] = 'aaa'
# # print(d.get('name'))
# # print(d.get('sex'))  # None
# print(d.get('sex', 'male'))  # male
