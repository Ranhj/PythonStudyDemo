# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/15 15:29
# IDE:        PyCharm
# Title:      func_lambda_parameterform_demo.py
# lambda的参数形式
# 1.无参数
fn1 = lambda: 100
print(fn1())                # 100

# 2.一个参数
fn2 = lambda a: a   # 冒号后面写a是为了验证返回的数据，可以根据具体情况写
print(fn2('hello'))         # hello

# 3.默认参数
fn3 = lambda a, b, c = 15: a + b - c
print(fn3(10, 20))          # 15    c没有传入数据就使用默认数据
print(fn3(100, 200, 150))   # 150   c传入了真实数据就会覆盖默认数据

# 4.可变参数： *args
fn4 = lambda *args: args        # 返回一个元组
print(fn4(1))               # (1,)
print(fn4(1, 2))            # (1, 2)
print(fn4(1, 2, 3))         # (1, 2, 3)

# 5.可变参数： **kwargs
fn5 = lambda **kwargs: kwargs   # 返回一个字典
print(fn5(name='Lucy'))                             # {'name': 'Jack'}
print(fn5(name='Jack', age=18))                     # {'name': 'Jack', 'age': 18}
print(fn5(name='Tom', age=200, hobby='guitar'))     # {'name': 'Tom', 'age': 200, 'hobby': 'guitar'}
