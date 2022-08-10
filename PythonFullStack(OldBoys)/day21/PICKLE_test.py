# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-06-20 10:13
# className:  PICKLE_test.py
import json
import pickle

def foo():
    print('ok')

data = pickle.dumps(foo)
f = open('PICKLE_text', 'wb')
f.write(data)
f.close()



