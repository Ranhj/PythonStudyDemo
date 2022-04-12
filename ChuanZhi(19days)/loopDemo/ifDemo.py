# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/1 14:12
'''
if 条件：
    条件成立执行的代码1
    。。。。。。
'''
# if True:
#     print('条件成立执行的代码1')
#     print('条件成立执行的代码2')
# # 注意：在这个下方的没有加缩进的代码，不属于if语句块，即和条件成立与否无关
# print('这个代码执行吗？')

# age = int(input('请输入您的真实年龄：'))
# # print(type(age))
# if age >= 18:
#     print('已经成年，可以提供上网服务！')
#     print('启动系统中~请稍等~~')
# else:
#     print('抱歉，你还是未成年，不能上网！')
#     print('关机！！！')

# age = float(input('请输入您的真实年龄：'))
# year = 18 - age
# if 18 <= age <= 120:
#     print(f'您输入的年龄是{age}，可以正常上网!')
# elif age <= 0 or age >= 120 :
#     print(f'您输入的年龄是{age}，输入有误，请检查后再次输入！')
# else:
#     print(f'抱歉！小朋友，您的年龄不满足上网要求哟！您还需要{year}年后才能上网！别想着吃鸡了，快回家做作业吧~~~')

# age = int(input('请输入一个年龄：'))
# # if 0 < age < 18:
# if (age > 0) and (age < 18):
#     print(f'你输入的年龄是{age}，该年龄段属于童工，不合法！')
# # elif 18 <= age <= 60:
# elif (age >= 18) and (age <= 60):
#     print(f'你输入的年龄是{age}，该年龄段为合法工作年龄')
# # elif 60 < age < 150:
# elif (age > 60) and (age < 150):
#     print(f'您输入的年龄是{age}，该年龄段为法定退休年龄')
# else:
#     print(f'您输入的年龄是{age}，您输入有误，请检查后重新再试！')

# money = float(input('请输入您身上的零钱数量：'))
# if money >= 2:
#     print(f'您的零钱有{money}元，可以上车')
#     seat = int(input('请输入空座个数：'))
#     if seat > 1:
#         print(f'车上有{seat}个座位，您可以找个座位坐下！')
#     else:
#         print(f'车上没有座位了，你还是站着吧~~~')
# else:
#     print(f'您的零钱只有{money}元，不够车票，还是下车走路吧！')


import random

player = int(input('请输入您要出的拳：0.石头  1.剪刀  2.布：'))
computer = random.choice(['石头','剪刀','布'])
# print(computer)
if (player == 0 and computer == '剪刀') or (player == 1 and computer == '布') or (player == 2 and computer == '石头'):
    print(f'当前局电脑出拳为{computer}，您出拳为{player},您获胜！')
elif (player == 2 and computer == '剪刀') or (player == 0 and computer == '布') or (player == 1 and computer == '石头'):
    print(f'当前局电脑出拳为{computer}，您出拳为{player},电脑获胜！')
elif player != (0, 1, 2):
    print('您输入有误！请重新开始游戏！')
else:
    print(f'当前局电脑出拳为{computer}，您出拳为{player}，平局！')
