# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/10 16:50
# IDE:        PyCharm
# Title:      func_documentation_demo.py
# help(len)   # help函数作用：查看函数的说明文档（函数的解释说明的信息）
def sum_num(a, b):
    """求和函数"""
    return a + b
# print(sum_num(1, 5))
help(sum_num)

def sum_num2(a, b):
    '''
    求和函数
    :param a:参数1
    :param b:参数2
    :return:返回值
    '''
help(sum_num)