# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-06-01 16:12
# className:  hashlib_module_demo.py
"""
hashlib模块：
    用于加密相关的操作，3.x 里代替了md5模块和sha模块，主要提供SHA1,SHA224,SHA256,SHA384,SHA512,MD5算法
"""
import hashlib

# m = hashlib.md5()
# print(m)    # <md5 HASH object @ 0x000001C439266A90>
#
# m.update('hello world'.encode('utf-8'))
# print(m.hexdigest())    # 5eb63bbbe01eeed093cb22bb8f5acdc3
# m.update('alex'.encode('utf-8'))
# print(m.hexdigest())    # 82bb8a99b05a2d8b0de2ed691576341a
#
#
# # 相当于拼接后加密
# m2 = hashlib.md5()
# m2.update('hello worldalex'.encode('utf-8'))
# print(m2.hexdigest())   # 82bb8a99b05a2d8b0de2ed691576341a
#
# mm = hashlib.md5()
# mm.update('ranhaijun'.encode())
# print(mm.hexdigest())   # 5cb93baa59204b2302178ef4706adc51

# s = hashlib.sha256()
# s.update('hello world'.encode('utf-8'))
# print(s.hexdigest())    # b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9

