# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/16 16:49
# IDE:        PyCharm
# Title:      file_readlines_demo.py

# readlines()
# readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
f = open('file4.txt', 'r')
content = f.readlines()
print(content)  # ['aaa\n', 'bbb\n', 'ccc\n', 'ddd\n', 'eee']
f.close()