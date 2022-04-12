# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/18 16:42
# IDE:        PyCharm
# Title:      cookpotato_demo.py

# 烤地瓜
# 1.定义类：初始化属性、被烤和添加调料的方法、显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 烤的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜的方法"""
        # 1. 先计算地瓜整体烤过的时间
        self.cook_time += time
        # 2. 用整体烤过的时间再判断地瓜的状态
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟的'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state = '烤糊了'

    def add_condiments(self, condiment):
        # 用户意愿的调料追加到调料列表
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜烤的时间有{self.cook_time}分钟了，状态是{self.cook_state},添加的调料有{self.condiments}'

# 2.创建对象并调用对应的实例方法
digua1 = SweetPotato()
print(digua1)
digua1.cook(2)
digua1.add_condiments('香油')

print(digua1)
digua1.cook(2)
digua1.add_condiments('椒盐')

print(digua1)
digua1.cook(2)
digua1.add_condiments('辣椒面')

print(digua1)
digua1.cook(2)
print(digua1)