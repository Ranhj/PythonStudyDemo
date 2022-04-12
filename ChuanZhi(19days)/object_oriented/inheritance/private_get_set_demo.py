# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/21 13:58
# IDE:        PyCharm
# Title:      private_get_set_demo.py
# 获取和修改私有属性的方法 get_xx  set_xx
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼]'
    def make_cake(self):
        print(f'使用{self.kongfu}制饼')

class Prentice(Master):
    def __init__(self):
        self.kongfu = '[自创煎饼]'

        # 定义私有属性
        self.__money = 10

    def make_cake(self):
        self.__init__()
        print(f'使用{self.kongfu}制饼')
    def master_make_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    # 定义函数：获取私有属性值  get_xx
    def get_money(self):
        return self.__money
    # 定义函数：修改私有属性值  set_xx
    def set_money(self):
        self.__money = 5000

class Tusun(Prentice):
    pass

tudi = Prentice()
tusun = Tusun()

print(tusun.get_money())    # 徒孙使用get方法获取私有属性__money初始值为10
tusun.set_money()           # 徒孙使用set方法修改私有属性的值
print(tusun.get_money())    # 徒孙修改之后的值为5000
