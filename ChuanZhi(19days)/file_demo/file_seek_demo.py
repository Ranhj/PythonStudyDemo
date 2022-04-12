# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/17 11:06
# IDE:        PyCharm
# Title:      file_seek_demo.py
"""
语法：文件对象.seek(偏移量， 起始位置)  起始位置：0开头位置 1当前位置 2结尾位置
目标：
    1.r 改变文件指针位置：改变读取数据开始位置或把文件指针放结尾（无法读取数据）
    2.a 改变文件指针位置，做到可以读取出来数据
"""
# f = open("file4.txt", "r+")
# # 1.改变读取数据开始位置
# # f.seek(3, 0)    # 从开头跳过前三个从第4个开始读取
# # 1.把文件指针放结尾（无法读取数据）
# f.seek(0, 1)
# content = f.read()
# print(content)
# f.close()

# 2. a 改变文件指针位置，做到可以读取出来数据
f = open("file4.txt", "a+")
# f.seek(0, 0)  # 读取了所有数据
f.seek(0)       # 读取了所有数据，可以省写
content = f.read()
print(content)
f.close()