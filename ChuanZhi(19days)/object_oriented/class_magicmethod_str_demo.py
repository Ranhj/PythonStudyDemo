# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/18 15:30
# IDE:        PyCharm
# Title:      class_magicmethod_str_demo.py

# 魔法方法  __str__()
# 当使用print输出对象的时候，默认打印对象的内存地址。
# 如果类定了__str__()方法，那么就会打印从在这个方法中return的数据
class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def washer(self):
        print(f'haier洗衣机的宽度是{self.width}, 高度是{self.height}')

    def __str__(self):
        # return '解释说明：类的说明或对象状态的说明'
        return '这是haier洗衣机的尺寸说明'

haier = Washer(300, 500)
haier.washer()
print(haier)