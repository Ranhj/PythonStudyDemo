# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-04-24 15:43
# className:  lesson_file.py
f1 = open("小重山", 'r', encoding='utf-8')
# data = f1.read()       # 《小重山·昨夜寒蛩不住鸣》
# data = f1.readline()     # 《小重山·昨夜寒蛩不住鸣》
# data = f1.readlines()     # ['《小重山·昨夜寒蛩不住鸣》\n', '昨夜，寒秋蟋蟀不住哀鸣，\n', '梦回故乡，千里燃战火，被惊醒，已三更。\n', '站起身，独绕台阶踽踽行。\n', '四周静悄悄，帘外，一轮淡月正朦胧。\n', '为国建功留青史，未老满头霜星星。\n', '家山松竹苍然老，无奈议和声起、阻断了归程。\n', '想把满腹心事，付与瑶琴弹一曲。\n', '可可高山流水知音稀，\n', '纵然弦弹断，\n', '又有谁来听？']
# # print(data)
# 遍历打印方法一
# number = 0
# for i in data:
#     # print(i, end='')
#     # print(i.strip())
#     # """---两种方法一样，打印效果如下---
#     # 《小重山·昨夜寒蛩不住鸣》
#     # 昨夜，寒秋蟋蟀不住哀鸣，
#     # 梦回故乡，千里燃战火，被惊醒，已三更。
#     # 站起身，独绕台阶踽踽行。
#     # 四周静悄悄，帘外，一轮淡月正朦胧。
#     # 为国建功留青史，未老满头霜星星。
#     # 家山松竹苍然老，无奈议和声起、阻断了归程。
#     # 想把满腹心事，付与瑶琴弹一曲。
#     # 可可高山流水知音稀，
#     # 纵然弦弹断，
#     # 又有谁来听？
#     # """
#     number += 1
#     if number == 10:
#         i = ''.join([i.strip(), '*****'])   # 取代万恶的连接符“+”
#     print(i.strip())
# 遍历打印方法二
# for i in f1:    # 这是for内部将f对象做成一个迭代器，用一行取一行
#     print(i.strip())    # 打印效果同上
print(f1.tell())
print(f1.read(5))
print(f1.tell())
f1.seek(0)
print(f1.read(12))
f1.close()
# f2 = open("小重山2", 'w+', encoding='utf-8')
# f2.write('Hello World\n')
# f2.write('Hi Python')
# f2.close()

# f3 = open("小重山3", "w+", encoding='utf-8')
# f3.write('a \n')
# f3.write('b \n')
# f3.write('c \n')
# f3.close()
