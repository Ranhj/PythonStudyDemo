# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/18 14:18
# IDE:        PyCharm
# Title:      class_leilimianhuoquduixiangshuxing_demo.py

# 类里面获取对象属性     self.属性名
class Washer():
    def print_info(self):
        # 在类里面获取实例属性
        print(f'haier洗衣机的宽度是：{self.width}')
        print(f'haier洗衣机的高度是：{self.height}')

# 创建对象
haier = Washer()

# 添加实例属性
haier.width = 500
haier.height = 800

haier.print_info()
