# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-06-20 10:05
# className:  json_test.py
# import json
# dic = {'name': 'alex', 'age': '18'}
# data = json.dumps(dic)
# f = open('JSON_text', 'w')
# f.write(data)
# f.close()

# def foo():
#     print('ok')
# data = json.dumps(foo)  # TypeError: Object of type function is not JSON serializable
# f = open('JSON_text', 'w')
# f.write(data)
# f.close()

# --------------dump---------------

import json
dic = {'name': 'alex', 'age': '18'}
f = open('JSON_test', 'w')
# data = json.dumps(dic)
# f.write(data)
json.dump(dic, f)
f.close()