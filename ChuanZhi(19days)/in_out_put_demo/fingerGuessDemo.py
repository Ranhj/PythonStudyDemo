# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/1 17:45
import random

player = int(input('请输入您要出的拳：0.石头  1.剪刀  2.布：'))
computer = random.choice(['石头','剪刀','布'])
# print(computer)
if (player == 0 and computer == '剪刀') or (player == 1 and computer == '布') or (player == 2 and computer == '石头'):
    print(f'当前局电脑出拳为{computer}，您出拳为{player},您获胜！')
elif (player == 2 and computer == '剪刀') or (player == 0 and computer == '布') or (player == 1 and computer == '石头'):
    print(f'当前局电脑出拳为{computer}，您出拳为{player},电脑获胜！')
elif (player != 0) and (player != 1) and (player != 2):
    print('您输入有误！请重新开始游戏！')
else:
    print(f'当前局电脑出拳为{computer}，您出拳为{player}，平局！')
