# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-08-18 17:12
# className:  lianxi01.py
class Foo:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def driver(self):
        print('%s,%s岁了,%s,喜欢开车出去浪' % (self.name, self.age, self.gender))
    def game(self):
        print('%s,%s岁了,%s,每天宅家玩游戏' % (self.name, self.age, self.gender))
    def drink(self):
        print('%s,%s岁了,%s,三更半夜逛酒吧' % (self.name, self.age, self.gender))

xm = Foo('小明', 18, '男')
xm.driver()
xm.game()
xm.drink()

xl = Foo('小丽', 20, '女')
xl.driver()
xl.game()
xl.drink()