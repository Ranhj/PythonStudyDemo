#!/usr/bin/env python
# -*_ coding:utf-8 _*_
# author:    冉海军
# datetime:  2022/2/27 16:01
# 文件名称:    geShiHuaPrintDemo.py
# IDE:       PyCharm

'''
1.准备数据
2.格式化符号输出数据
'''
age = 18
name = 'TOM'
weight = 75.545
stu_id = 1
stu_id2 = 1001
stu_id3 = 1002
# 1.今年我的年龄是X岁 --整数  %d
print("今年我的年龄是%d" % age)
# 2.我的名字是X
print('我的名字是%s' % name)
# 语法 f'{}'
print(f'我的名字是{name}')
# 3.我的体重是X公斤    %.2f 表示小数点后显示的小数位数  超出的位数四舍五入
print('我的体重是%.2f' % weight, '公斤')
# 4.我的学号是X
print('我的学号是%d' % stu_id)
# 4.1我的学号是001   %03d  表示输出的整数显示位数，不足以0不全，超出当前位数则原样输出
print('我的学号是%03d'% stu_id)
print('我的学号是%03d'% stu_id2)
print('我的学号是%06d'% stu_id3)
# 5.我的名字是X，明年X岁了
print('我的名字是%s,明年%d岁了' % (name, age+1))
# 6，我的名字是X，今年X岁了，体重是X公斤，学号是
print('我的名字是%s,今年%d岁了，体重是%.2f公斤，学号是%04d' % (name, age, weight, stu_id))
print(f'我的名字是{name},后年就{age+2}岁了，体重是{weight}公斤，学号是{stu_id}')