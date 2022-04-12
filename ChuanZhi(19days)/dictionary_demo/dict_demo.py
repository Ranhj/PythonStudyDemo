# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/23 17:53
# IDE:        PyCharm
# Title:      dict_demo.py

# __dict__
# 1.定义类
class A(object):
    a = 5   # 定义一个类属性 a
    def __init__(self):
        self.b = 2  # 定义一个实例属性 b

# 2.创建对象
aa = A()

# 调用__dict__       返回的结果都是字典
# 返回类内部所有属性和方法对应的字典
print(A.__dict__)   # {'__module__': '__main__', 'a': 5, '__init__': <function A.__init__ at 0x018B6070>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

# 返回实例属性和值组成的字典
print(aa.__dict__)  # {'b': 2}