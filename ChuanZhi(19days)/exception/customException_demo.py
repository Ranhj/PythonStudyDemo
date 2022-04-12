# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/22 14:40
# IDE:        PyCharm
# Title:      customException_demo.py
# 自定义异常
# 在python中，抛出自定义异常的语法为 ： raise 异常类对象
# 需求：密码长度不足，则报异常(用户输入密码，如果输入的长度不足3位，则报错，即抛出自定义异常，并捕获该异常)
# 1.自定义异常类， 继承Exception， 魔法方法有init和str(设置异常描述信息)
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        # 用户输入的密码长度
        self.length = length
        # 系统要求的最少长度
        self.min_len = min_len

    # 设置异常描述信息
    def __str__(self):
        return f'您输入的密码长度是{self.length}个字符,不能少于{self.min_len}个字符'

def main():
    try:
        pw = input('请输入密码:')
        if len(pw) < 3:
            # 2. 抛出异常
            raise ShortInputError(len(pw), 3)
    # 3.捕获该异常
    except Exception as result:
        print(result)
    else:
        print('没有异常，密码输入成功')

main()