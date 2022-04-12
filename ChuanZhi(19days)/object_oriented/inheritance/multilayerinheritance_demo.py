# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/21 9:30
# IDE:        PyCharm
# Title:      multilayerinheritance_demo.py
# 多层继承
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼')

class School(object):
    def __init__(self):
        self.kongfu = '黑马煎饼'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼')

class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '独创煎饼'
    def make_cake(self):
        self.__init__()
        print(f'使用{self.kongfu}制作煎饼')

    def master_make_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)

# 步骤：
# 1.创建类Tusun,用这个类创建对象
# 2.用这个对象调用父类的属性或方法看能否成功
class Tusun(Prentice):
    pass

xiaoC = Tusun()
print(xiaoC.kongfu)         # 独创煎饼
xiaoC.make_cake()           # 使用独创煎饼制作煎饼
xiaoC.master_make_cake()    # 使用古法煎饼制作煎饼
xiaoC.school_make_cake()    # 使用黑马煎饼制作煎饼