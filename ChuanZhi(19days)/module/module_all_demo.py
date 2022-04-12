# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/23 13:47
# IDE:        PyCharm
# Title:      module_all_demo.py
# __all__
# 如果一个模块文件中有__all__变量，当使用from xxx import * 导入时，只能导入这个列表中的元素
from my_module2 import *
testA()     # testA

# 因为testB函数没有添加到all列表，只有all列表里的功能才能导入
# testB()     # NameError: name 'testB' is not defined