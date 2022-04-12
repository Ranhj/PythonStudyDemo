# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/17 10:40
# IDE:        PyCharm
# Title:      file_zhufangwenmoshi_demo2.py
"""
测试目标：
    1. r+ 和 w+ a+ 区别：
    2. 文件指针对数据读取的影响
"""

# # r+ ： r没有该文件则报错；文件指针在开头，所以能读取出来数据

# # f = open("file5.txt", 'r+')     # file5.txt文件不存在，所以r+也会报错
# f = open("file4.txt", "r+")     # # file4.txt文件存在，所以r+读取正常
# content = f.read()
# print(content)
# """
# 打印信息：
# aaa
# bbb
# ccc
# ddd
# eee
# """
# f.close()


# # w+：没有该文件时会新建文件；w特点： 文件指针在开头，用新内容覆盖了原内容

# # f = open("file5.txt", "w+")     # file5.txt文件不存在，w+没有报错，而是创建了一个file5.txt文件
# f = open("file4.txt", "w+")     # w+ 覆盖了file4.txt原有的内容
# content = f.read()
# print(content)
# f.close()


# a+：没有该文件会新建文件；文件指针在结尾，无法读取数据（文件指针后面没有数据）

# f = open("file6.txt", "a+")     # file6.txt文件不存在，a+没有报错，而是创建了一个file6.txt文件
f = open("file4.txt", "a+")     # file4.txt文件是有内容的，但是因为文件指针在末尾，所以未读取到数据
content = f.read()
print(content)
f.close()