# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/18 15:13
# IDE:        PyCharm
# Title:      class_magicmethod_init_chuancan_demo.py

# 1.定义类：带参数的init：宽度和高度； 实例方法：调用实例属性
class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}， 洗衣机的高度是{self.height}')

# 2.创建对象，创建多个对象且属性值不同；  调用实例方法
haier = Washer(500, 800)
haier.print_info()

LG = Washer(300, 500)
LG.print_info()