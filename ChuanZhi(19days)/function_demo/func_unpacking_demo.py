#!/usr/bin/env python
# -*_ coding:utf-8 _*_
# author:    冉海军
# datetime:  2022/3/13 11:35
# 文件名称:    func_unpacking_demo.py
# IDE:       PyCharm

print('-'*10, '拆包：元组', '-'*10,)

# 拆包：元组数据
def return_num():
    return 100, 200
num1, num2 = return_num()
print(num1)     # 100
print(num2)     # 200

print('-'*10, '拆包：字典', '-'*10,)

# 拆包：字典数据，      对字典进行拆包，变量存储的数据是key值
# 先准备字典，然后拆包
dict1 = {'name': 'Jack', 'age': 18}
# dict1中有两个键值对，拆包的时候用两个变量去接收数据
a, b = dict1
print(a)            # name
print(b)            # age
print(dict1[a])     # Jack
print(dict1[b])     # 18