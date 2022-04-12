# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/19 16:18
# IDE:        PyCharm
# Title:      multipleinheritance_subclassoverwrite_demo2.py
# 子类调用父类的同名方法和属性
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼]'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼]'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 定义徒弟类，继承师傅类 和 学校类 ，添加和父类同名的属性和方法
class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '[独创煎饼]'
    def make_cake(self):
        # 如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己子类的初始化
        self.__init__()  # 这里加自己的初始化的原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值；如果先调用父类的再调用自己的，就会发现实际调用的还是父类的；如果加了，先调用父类的再调用自己的，就是自己的了
        print(f'使用{self.kongfu}制作煎饼果子')

    # 调用父类方法，但是为保证调用到的也是父类的属性，必须在调用方法前调用父类的初始化
    # 子类调用父类的同名属性和方法：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        # 父类类名.函数()
        Master.__init__(self)   # 再次初始化的原因：这里想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

xiaoC = Prentice()

xiaoC.make_master_cake()
xiaoC.make_school_cake()
xiaoC.make_cake()

