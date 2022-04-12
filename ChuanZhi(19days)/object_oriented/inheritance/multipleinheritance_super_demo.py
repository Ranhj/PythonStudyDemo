# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/21 9:54
# IDE:        PyCharm
# Title:      multipleinheritance_super_demo.py
"""
多层继承  super()
1. 带参写法   super(当前类名， self).函数()
2. 无参写法   super().函数()
注意：
    使用super()可以自动查找父类。调用顺序遵循 __mro__ 类属性的顺序。比较适合单继承使用
"""
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼]'
    
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼')
        
class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼]'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼')
        # 2.1 super()带参数写法
        # super(School, self).__init__()
        # super(School, self).make_cake()

        # 2.2 super()无参数写法
        super().__init__()
        super().make_cake()

class Prentice(School):
    def __init__(self):
        self.kongfu = '[自创煎饼]'
    def make_cake(self):
        self.__init__()
        print(f'使用{self.kongfu}制作煎饼')
    def master_make_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)

    # 需求： 一次性调用父类School  Master的方法
    def make_old_cake(self):
        # 方法一：如果定义的类名修改，这里也要修改，麻烦，代码庞大 冗余
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        # 方法二： super()
        # 2.1 super带参写法  super(当前类名， self).函数()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        # 2.2 super无参数写法
        super().__init__()
        super().make_cake()

xiaoA = Prentice()
xiaoA.make_old_cake()
