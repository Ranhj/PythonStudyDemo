# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/2 11:42
# 直接增量+2
i = 0
result = 0
while i <= 100:
    result += i
    i += 2
print(result)

# 判断是偶数再加
j = 0
result2 = 0
while j <= 100:
    if j % 2 == 0:
        result2 += j
    j += 1
print(result2)
