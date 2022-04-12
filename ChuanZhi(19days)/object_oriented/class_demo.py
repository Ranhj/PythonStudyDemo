# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/18 10:32
# IDE:        PyCharm
# Title:      class_demo.py
# 需求：洗衣机， 功能：能洗衣服
# 1.定义洗衣机类
"""
class 类名():
    代码
"""
class Washer():
    def wash(self):
        print('能洗衣服')
# 2.创建对象
# 对象名 = 类名()
haier = Washer()

# 3.验证成果
print(haier)    # <__main__.Washer object at 0x012E1FB8>

# 使用wash功能 --实例方法/对象方法  --对象名.wash()
haier.wash()    # 对象名去调用方法： 能洗衣服
