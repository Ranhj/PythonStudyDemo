#!/usr/bin/env python
# -*_ coding:utf-8 _*_
# author:    冉海军
# datetime:  2022/3/2 0:21
# 文件名称:    guessNumDemo.py
# IDE:       PyCharm
import random
# 电脑
computer = random.randint(0,2)
# 玩家
player = int(input('请输入您要出的拳：0.石头  1.剪刀  2.布：'))

if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 3):
    print(f'电脑出拳{computer}，玩家出拳{player}，玩家获胜！')
elif player == computer:
    print(f'电脑出拳{computer}，玩家出拳{player}，平局！')
else:
    print(f'电脑出拳{computer}，玩家出拳{player}，电脑获胜！')
