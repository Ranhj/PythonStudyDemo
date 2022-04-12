#!/usr/bin/env python
# -*_ coding:utf-8 _*_
# author:    冉海军
# datetime:  2022/3/13 17:32
# 文件名称:    func_quote_demo.py
# IDE:       PyCharm
# 在python中，值是靠引用来传递来的
# 可以用id()来判断两个变量是否为同一个值的引用   id()检测两个变量的id值（内存的十进制值）
print('-'*10, 'int类型', '-'*10)
# 1.int类型
a = 1
b = a
print(b)    # 1
print(id(a))    # 140706089325600
print(id(b))    # 140706089325600

a = 2
print(b)    # 1, 说明int类型为不可变类型
print(id(a))    # 140706089325632

print('-'*10, 'list类型', '-'*10)
# 2.列表 list
aa = [10, 20]
bb = aa
print(id(aa))   # 1961937625672
print(id(bb))   # 1961937625672

aa.append(30)
print(aa)       # [10, 20, 30]
print(bb)       # [10, 20, 30], 列表为可变类型
print(id(aa))   # 1312440803912
print(id(bb))   # 1312440803912
