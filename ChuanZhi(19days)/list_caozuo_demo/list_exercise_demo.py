# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/5 15:31
# IDE:        PyCharm
# className:  list_exercise_demo.py

# 需求：8位老师，3个办公室，将8位老师随机分配到3个办公室
'''
步骤：
1.准备数据
    1.1 8位老师--列表
    1.2 3个办公室 --列表嵌套
2.分配老师到办公室
    ***随机分配
    就是把老师的名字写入到办公室列表 --办公室列表追加老师名字数据
3.验证是否分配成功
    打印办公室详细信息：每个办公室的人数和对应的老师名字
'''
import random
# 1.准备数据
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]
# 2.遍历 分配老师到办公室  取到每个老师放到办公室列表  遍历老师列表数据
for name in teachers:
    # 列表追加数据  append、extend、insert
    # xx[0]--不能指定是具体某个下标，要随机分配到办公室
    num = random.randint(0, 2)  # 在三个办公室之间随机取一个下标
    offices[num].append(name)   # 将遍历到的老师名字追加到随机办公室
# print(offices)
# 为了更贴合生活，把各个办公室子列表加一个办公室编号：1，2，3
i = 1
# 3.验证是否分配成功
for office in offices:
    # 打印办公室人数 --子列表数据的个数 len()
    print(f'办公室{i}人数：{len(office)}人, 办公室老师名单：')
    # 打印老师的名字
    # print() -- 每个子列表里面的名字个数不一定，遍历，子列表
    for name in office:
        print(name)
    i += 1