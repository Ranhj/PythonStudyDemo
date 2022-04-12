# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/14 9:27
# IDE:        PyCharm
# Title:      func_quote_demo2.py
# 需求：引用是否可以当作实参
'''
1.定义函数：有形参
    1.1 访问打印形参看是否有数据
    1.2 访问形参的id
    1.3 改变形参的数据，查看这个形参并打印id，看id值是否相同
2.调用函数  --把可变和不可变两种类型依次当作实参传入

'''
def test1(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))

# b = 100
# test1(b)
'''
100
2067377632
200
2067379232
'''

c = [11, 22]
test1(c)
'''
[11, 22]
33086952
[11, 22, 11, 22]
33086952
'''
