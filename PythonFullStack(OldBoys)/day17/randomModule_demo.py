# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-23 17:21
# className:  randomModule_demo.py
# 随机数

import random
# print(random.random())      # 0-1的随机数  0.3278508668307235
# print(random.randint(1, 8))     # 1-8的随机数，包括8
# print(random.choice('hello'))   # l
# print(random.choice(['123', 4, [1, 2]]))    # 123

# print(random.randrange(1, 3))   # 1  这种随机结果不包含3，与random.randint()的区别

# 方法一
# def v_code():
#     code=''
#     for i in range(5):
#         if i == random.randint(0, 3):
#             add = random.randrange(10)
#         else:
#             add = chr(random.randrange(65, 91))
#         code += str(add)
#     print(code)
# v_code()

# 方法二
def v_code():
    code=''
    for i in range(5):
        add = random.choice([random.randrange(10),chr(random.randrange(65, 91))])
        # if i == random.randint(0, 3):
        #     add = random.randrange(10)
        # else:
        #     add = chr(random.randrange(65, 91))
        code += str(add)
    print(code)
v_code()


# print(chr(90))  # Z