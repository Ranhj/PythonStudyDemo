# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/19 9:54
# IDE:        PyCharm
# Title:      movehouse_demo.py
class BanJiaJu():
    def __init__(self):
        self.housePlace = '重庆'
        self.houseArea = 100
        self.jiajuArea = 0
        self.houseAreaYu = self.houseArea - self.jiajuArea
        self.jiajus = []


    def addjiajus(self, jiaju):
        self.jiajus.append(jiaju)

    def banJia(self, jiaju, jiajuArea):
        self.houseArea -= self.jiajuArea
        self.jiajuArea += self.jiajuArea
        if self.houseAreaYu > self.jiajuArea:
            return self.jiajus()

    def __str__(self):
        return f'房子还剩面积{self.houseArea}, 搬进的家具有{self.jiajus}'

bj = BanJiaJu()
print(bj)

