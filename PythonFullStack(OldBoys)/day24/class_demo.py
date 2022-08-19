# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-08-16 10:46
# className:  class_demo.py
# class Bar:
#     def foo(self, arg):
#         print(self, self.name, self.age, self.gender, arg)

# z1 = Bar()
# print(z1)
# ret1 = z1.foo(111)
#
# print("===================")
#
# z2 = Bar()
# print(z2)
# ret2 = z2.foo(222)

# z = Bar()
# z.name = 'alex'
# z.age = 20
# z.gender = '男'
# z.foo(666)
#
# z1 = Bar()
# z1.name = 'sniper'
# z1.age = 18
# z1.gender = '男'
# z1.foo(888)

# 构造方法
# 创建类，一般把公有的需要先创建好的，先放到init类里面
# class Bar:
#     def __init__(self, name, age):
#         # self=z,name=alex,age=18
#         """
#         构造方法
#         """
#         self.n = name
#         self.a = age
#
#
#     def foo(self):
#         print(self.n, self.a)
#
# z = Bar('alex', 18)
# z.foo()
# print(z.n)
# print(z.a)
# # z.n = 'alex'
# # z.a = 18

# class Person:
#     def __init__(self, name, age):
#         """
#         构造方法：特性是  类名() 就可以自动执行构造方法
#         """
#         self.n = name
#         self.a = age
#         self.x = 'o'    # 某些属性是公共的的，可以直接写死
#
#     def show(self):
#         print('%s-%s-%s' % (self.n, self.a, self.x))
#
# lily = Person('丽丽', 19)
# lily.show()     # 丽丽-19-o
#
# Jeck = Person('杰克', 20)
# Jeck.show()     # 杰克-20-o

class DateBaseHelper:
    def __init__(self, ip, port, username, pwd):
        self.ip = ip
        self.port = port
        self.username = username
        self.pwd = pwd

    def add(self, content):
        # 利用self中封装的用户名、密码等，链接数据库
        print(self.ip, self.port, self.username, self.pwd)
        # 关闭数据链接

    def delete(self, content):
        pass
    def update(self, content):
        pass
    def get(self, content):
        pass
obj = DateBaseHelper('127.0.0.1', '80', 'abc', '123')
obj.add('aaa')
obj.delete('bbb')
obj.update('ccc')
obj.get('ddd')