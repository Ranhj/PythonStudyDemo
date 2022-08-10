# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-06-20 10:18
# className:  PICKLE_load.py
import pickle
def foo():
    print('ok')

f = open('PICKLE_text', 'rb')
data = f.read()
data = pickle.loads(data)
data()