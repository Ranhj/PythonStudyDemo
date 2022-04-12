# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/21 10:57
# IDE:        PyCharm
# Title:      private_demo.py
# 定义私有权限的方法：    在属性名和方法名前面加上两个下划线 __
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼]'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼')

class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼]'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼')
        super().__init__()
        super().make_cake()

class Prentice(School):
    def __init__(self):
        self.kongfu = '[独创煎饼]'
        self.__money = '2000个亿'     # 属性前加两个下划线__  定义私有属性
    # 定义私有方法    方法名前加两个下划线__
    # def __info_print(self):
    #     print('这是私有方法')

    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼')

    def make_old_cake(self):
        super().__init__()
        super().make_cake()
class Tusun(Prentice):

    pass


xiaoC = Tusun()
# print(xiaoC.__money)
# print(xiaoC.kongfu)
# xiaoC.info_print()
