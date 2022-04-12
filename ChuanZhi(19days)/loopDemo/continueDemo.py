# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/2 14:51
i = 1
while i <= 5:
    print(f'开始吃第{i}个苹果！')
    if i == 3:
        print(f'第{i}个苹果是坏的，扔了继续吃第{i+1}个苹果吧！')
        # 如果使用continue，在continue之前一定要修改计数器，否则将进入死循环！！！
        i += 1
        continue
    print(f'吃了{i}个苹果！')
    i += 1




