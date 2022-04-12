# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/18 11:17
# IDE:        PyCharm
# Title:      class_self_demo2.py
# 1.验证一个类是否可以创建多个对象     --可以
# 2.多个对象都调用函数的时候，函数里的self地址是否相同     --每个对象的self地址不相同，但是和相应的对象的地址相同

class Washer():
    def wash(self):
        print('我会洗衣服')
        print(f'self的内存地址是:{self}')
print('-'*10, 'haier.wash()', '-'*10)
haier = Washer()
haier.wash()
print(f'haier的内存地址是：{haier}')

print('-'*10, 'LG.wash()', '-'*10)
LG = Washer()
LG.wash()
print(f'LG的内存地址是：{LG}')