# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/18 14:41
# IDE:        PyCharm
# Title:      class_magicmethod_init_demo.py
#   魔法方法    __init__()
# 在python中，__xx__()的函数叫做魔法方法，指的是具有特殊功能的函数
# __init__() 方法的作用是： 初始化对象
# __init__()方法，在创建一个对象时默认被调用，不需要手动调用
# __init__()方法中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去

# 目标：定义init魔法方法设置初始化属性，并访问调用
"""
1. 定义类
    init魔法方法： width 和 height
    添加实例方法：  访问示例属性

2. 创建对象

3. 验证成果
    调用实例方法
"""
class Washer():
    def __init__(self):
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'haier洗衣机的宽度是：{self.width}')
        print(f'haier洗衣机的高度是：{self.height}')

haier = Washer()

haier.print_info()
