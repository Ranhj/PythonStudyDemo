# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/3 10:46
str1 = 'Hello Python'
for i in str1:
    if i == 'e':
        print('遇到 e 时不打印')
        # break
        continue
    print(i)

else:
    print('循环正常结束后执行的else的代码')
