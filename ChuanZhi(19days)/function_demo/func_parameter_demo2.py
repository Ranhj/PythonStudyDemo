# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 15:46
# IDE:        PyCharm
# Title:      func_parameter_demo2.py
# 函数调用，通过”键=值“形式加以指定，可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求
# 注意：函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数直接不存在先后顺序

def user_info(name, age, hobby):
    print(f'您的名字是{name},年龄是{age}岁，爱好是{hobby}')

user_info('Jack', hobby='guitar', age=19)           # 您的名字是Jack,年龄是19岁，爱好是guitar
user_info(hobby='画画', age=20, name='Lily')         # 您的名字是Lily,年龄是20岁，爱好是画画
# 位置参数必须对应位置
# user_info('画画', age=20, name='Lily')         # 报错：TypeError: user_info() got multiple values for argument 'name'
# 位置参数必须写在关键字参数的前面
# user_info(age=20, name='Lily', 'Tom')         # 报错：SyntaxError: positional argument follows keyword argument
