# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/10 17:16
# IDE:        PyCharm
# Title:      func_qiantaodiaoyong_demo2.py
def print_line():
    print('-'*20)

def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1
print_lines(6)