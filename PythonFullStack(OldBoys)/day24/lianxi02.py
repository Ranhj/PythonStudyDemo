# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-08-18 17:39
# className:  lianxi02.py
from time import sleep

print('---------------多人PK游戏---------------')
class Game:
    def __init__(self, name, gender, age, fight):
        self.name = name
        self.gender = gender
        self.age = age
        self.fight = fight

    def caocongzhandou(self):
        print(self.name, '开启草丛战斗模式，消耗200战斗力')
        self.fight -= 200

    def ziwoxiulian(self):
        print(self.name, '累了，自我修炼恢复下，增长100战斗力！')
        self.fight += 100

    def duorenyouxi(self):
        print(self.name, '来了，加入多人游戏，消耗500战斗力！')
        self.fight -= 500

    def chushizhankuang(self):
        temp = ('姓名：%s,性别：%s,年龄%s岁,初始战斗力：%s' % (self.name, self.gender, self.age, self.fight))
        print(temp)

    def zuizhongzhankuang(self):
        temp1 = ('姓名：%s,性别：%s,年龄%s岁,最终战斗力：%s' % (self.name, self.gender, self.age, self.fight))
        print(temp1)

cang = Game('苍老师', '女', 20, 1500)
bo = Game('波老师', '女', 21, 2000)
qin = Game('秦杨', '男', 18, 1000)
cang.chushizhankuang()
bo.chushizhankuang()
qin.chushizhankuang()
sleep(1)
print('----------------------------')
sleep(1)
cang.caocongzhandou()
sleep(1)
qin.caocongzhandou()
sleep(1)
print('----------------------------')
sleep(1)
cang.ziwoxiulian()
sleep(1)
print('----------------------------')
sleep(1)
bo.duorenyouxi()
sleep(1)
print('----------------------------')
print('秦杨受不了，缴械投降了。。。')
sleep(1)
print('-------------最终战绩---------------')
sleep(1)
cang.zuizhongzhankuang()
bo.zuizhongzhankuang()
qin.zuizhongzhankuang()