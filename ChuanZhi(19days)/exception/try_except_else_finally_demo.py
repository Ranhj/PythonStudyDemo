# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/22 11:11
# IDE:        PyCharm
# Title:      try_except_else_finally_demo.py
# 异常的finally
# finally表示的是无论是否异常都要执行的代码，例如关闭文件
try:
    f = open('test.txt', 'r')
except Exception as result:
    f = open('test.txt', 'w')
else:
    print('没有出现错误')
finally:
    f.close()