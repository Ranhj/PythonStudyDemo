# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-06-20 10:09
# className:  JSON_loads.py

import json
f = open('JSON_text', 'r')
# data = f.read()
# data = json.loads(data)

data = json.load(f)
print(data['name'])