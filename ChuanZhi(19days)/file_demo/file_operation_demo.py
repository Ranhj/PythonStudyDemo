# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/16 15:28
# IDE:        PyCharm
# Title:      file_operation_demo.py
# 文件的基本操作
# 1.打开（新建）
'''
open(name, mode) :
    name:是要打开的目标文件名的字符串(可以包含文件所在的具体路径)，如果该文件不存在，则会新建文件
    mode:设置打开文件的模式(访问模式)：只读、写入、追加等
'''
f = open('file1', 'w', encoding='utf-8')
# 2. 读写操作  read()   write()
f.write('Hello, 冉sir')
# 3.关闭 close()
f.close()
