# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/18 11:35
# IDE:        PyCharm
# Title:      class_leiwaimiantianjiahehuoquduixiangshuxing_demo.py
class Washer():
    def wash(self):
        print('洗衣服')

haier = Washer()

# 类外面添加属性
# 语法：   对象名.属性名 = 值
haier.width = 500
haier.height = 800

# 类外面获取对象属性
# 语法：  对象名.属性名
print(f'haier洗衣机的宽度是：{haier.width}')
print(f'haier洗衣机的高度是：{haier.height}')
