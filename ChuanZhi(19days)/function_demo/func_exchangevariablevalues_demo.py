#!/usr/bin/env python
# -*_ coding:utf-8 _*_
# author:    冉海军
# datetime:  2022/3/13 11:50
# 文件名称:    func_exchangevariablevalues_demo.py
# IDE:       PyCharm

# 交换变量值
# 需求： 有变量a = 10 和 b = 20 交换两个变量的值
print('-'*10, '第一种方法', '-'*10)
# 方法一：借助第三变量存储数据
a = 10
b = 20
# 1.定义中间变量
c = 0
# 2.将a的数据存储到c
c = a
# 3.将b的数据20赋值到a，此时a = 20
a = b
# 4.将之前c的数据10赋值到b，此时b = 10
b = c

print(a)    # 20
print(b)    # 10

print('-'*10, '第二种方法', '-'*10)

# 方法二：
aa, bb = 10, 20
aa, bb = bb, aa
print(aa)   # 20
print(bb)   # 10
