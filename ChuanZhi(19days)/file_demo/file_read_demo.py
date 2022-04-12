# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/16 16:41
# IDE:        PyCharm
# Title:      file_read_demo.py

# read()
# 文件对象.read(num)    num表示要从文件中读取的数据的长度(单位是字节)，如果没有传入num，那么就表示读取文件中所有的数据

f = open('file4.txt', 'r')

# print(f.read())   # read不写参数表示读取所以数据
print(f.read(10))   # 文件内容如果换行，底层有\n，会有字节占位，导致read书写参数读取出来的眼睛看到的个数和参数值不匹配

f.close()