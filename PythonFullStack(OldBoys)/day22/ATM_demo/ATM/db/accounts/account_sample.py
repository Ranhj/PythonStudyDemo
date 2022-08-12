# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-08-11 16:34
# className:  account_sample.py

import json
acc_dic = {
    'id': '0001',
    'password': 'Qq1234',
    'credit': 1000,     # 信用额度
    'balance': 1000,    # 余额
    'enroll_date': '2022-08-11',    # 注册
    'expire_date': '2023-08-11',    # 到期
    'pay_day': 27,  # 还款日期
    'status': 0     # 0 = normal, 1 = locked, 2 = disabled
}

print(json.dumps(acc_dic))

