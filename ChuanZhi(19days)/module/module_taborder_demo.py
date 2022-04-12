# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/23 10:37
# IDE:        PyCharm
# Title:      module_taborder_demo.py
# 模块定位顺序
"""
当导入一个模块，python解析器对模块位置的搜索顺序是：
1.当前目录
2.如果不在当前目录，python则搜索在shell变量PYTHONPATH下的每个目录
3.如果都找不到，python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python

模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录

注意：
    自己的文件名不要和已有模块名重复，否则导致模块功能无法使用
    使用from 模块名 import 功能的时候，如果功能名字重复，调用到的是最后定义或导入的功能
"""

# 1.自己的文件名不能和已有模块名重复，如果重复将导致模块无法使用  --random
# import random
# num = random.randint(1, 5)
# print(num)  # AttributeError: module 'random' has no attribute 'randint'
# 自己在当前目录写了一个random模块后再导入，因为模块定位顺序是由近至远的原则，
# 优先调用当前目录自己写的模块，而模块里面啥都没有，所以会报错


# 2.当使用from xx import 功能 导入模块的功能的时候，如果功能名字重复，导入的时候后定义或后导入的这个同名功能
# 场景  time.sleep()
# def sleep():
#     print('我的自己写的sleep功能')
#
# from time import sleep
#
# sleep(2)


# 拓展： 名字重复
# 问题： import 模块名 是否担心 功能名字重复的问题  --不需要
import time
print(time)     # <module 'time' (built-in)>

time = 1
print(time)     # 1
# 问题： 为什么变量也能覆盖模块？
#   --在python语言中，数据是通过 引用 传递的。  要避免名字重复，非常可怕！