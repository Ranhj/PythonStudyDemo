# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/19 15:39
# IDE:        PyCharm
# Title:      singleinheritance_demo.py
# 单继承
# 1.师傅类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼]'

    def make_bing(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 2.定义徒弟类，继承师傅类
class Prentice(Master):
    pass

# 3.用徒弟类创建对象，调用实例属性和方法
xiaoming = Prentice()
print(xiaoming.kongfu)
xiaoming.make_bing()

