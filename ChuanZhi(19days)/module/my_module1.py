# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/23 9:42
# IDE:        PyCharm
# Title:      my_module1.py
# 需求：一个函数，完成任意两个数字的加法运算
def testA(a, b):
    print(a + b)


# 测试信息
# testA(1, 2)

# __name__是系统变量，是模块的标识符，值是：如果是自身模块值是__main__，否则是当前的模块的名字

# print(__name__)     # __name__：如果当前是在自己模块内被调用就是：__main__； 如果是在其他模块被调用则是被调用模块名：my_module1

# 只在当前文件中调用该函数，其他导入的文件内不符合该条件，则不执行testA函数调用
if __name__ == '__main__':
    testA(11, 12)           # 23