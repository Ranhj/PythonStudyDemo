# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/3 9:53
# i = 0
# while i < 5:
#     print('媳妇儿，我错了！')
#     i += 1
# else:
#     print('原谅你了！')

i = 1
while i <= 5:
    if i == 3:
        print(f'第{i}遍道歉一点都不真诚，我不想听了！')
        #
        i += 1
        continue
    print(f'第{i}遍道歉：媳妇儿，我错了！')
    i += 1
else:
    print('媳妇儿终于原谅我了~~~')