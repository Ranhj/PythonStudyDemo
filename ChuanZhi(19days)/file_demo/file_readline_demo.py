# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/16 17:02
# IDE:        PyCharm
# Title:      file_readline_demo.py
# readline()  一次读取一行内容
f = open('file4.txt', 'r')
content = f.readline()
print(f'第一行：{content}', end='')

content = f.readline()
print(f'第二行：{content}')

content = f.readline()
print(f'第三行：{content}')

f.close()