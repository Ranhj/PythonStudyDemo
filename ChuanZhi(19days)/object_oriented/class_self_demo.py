# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/18 11:11
# IDE:        PyCharm
# Title:      class_self_demo.py
# self  指的是调用该函数的对象
class Washer():
    def wash(self):
        print('洗衣服')    # 洗衣服
        print(self)     # <__main__.Washer object at 0x0105B028>

haier = Washer()
print(haier)            # <__main__.Washer object at 0x0105B028>
haier.wash()

# 由于打印对象和打印self所得到的内存地址是相同的，所以self指的是调用该函数的对象
