# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/2/28 15:11
'''
1. 书写input
    input('提示信息')
2. 观察特点：
    2.1 遇到input，等待用户输入
    2.2 接收input存变量
    2.3 input接收到的数据类型都是字符串
'''
# password = input('请输入您的密码：')
# print(f'您输入的密码是：{password}')
# print(type(password))

num = int(input('请输入一个数字：'))
print(num)
print(type(num))

num2 = input("请输入一个数字：")
print(num2)
print(type(int(num2)))

num3 = input("请输入一个数字：")
print(num3)
print(type(float(num3)))

