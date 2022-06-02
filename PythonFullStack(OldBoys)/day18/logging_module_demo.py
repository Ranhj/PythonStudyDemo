# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-06-02 9:24
# className:  logging_module_demo.py
"""
logging模块：
    很多程序都有记录日志的需求，并且日志中包含的信息既有正常的程序访问日志，还可能有错误、警告等信息输出，
python的logging模块提供了标准的日志接口，可以通过它存储各种格式的日志
    logging的日志可以分为5个级别： debug(), info(), warning(), error(), critical()
"""

import logging
# logging.warning('user [alex] attempted wrong password more than 3 times')
# logging.critical('server is down')



logging.basicConfig(
    level=logging.DEBUG,    # 设置rootlogger的日志级别
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',     # 指定handler使用的日志显示格式
    datefmt = '%a, %d %b %Y %H :%M:%S',     # 指定日期时间格式
    # filename = r'D:\Study\dirname1\dirname2\test.log',
    filename = 'test.log',  # 用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中
    filemode = 'w')     # 文件打开方式，在指定了filename时使用这个参数，默认值为"a"还可指定为"w"
# stream 用指定的stream创建StreamHandler，可以指定输出到sys.stderr, sys.stdout或者文件，默认为sys.stderr,
# 若同时列出了filename和stream两个参数，则stream参数会被忽略


logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')  # WARNING:root:warning message
logging.error('error message')      # ERROR:root:error message
logging.critical('critical message')    # CRITICAL:root:critical message

"""
Thu, 02 Jun 2022 15 :31:35 logging_module_demo.py[line:26] DEBUG debug message
Thu, 02 Jun 2022 15 :31:35 logging_module_demo.py[line:27] INFO info message
Thu, 02 Jun 2022 15 :31:35 logging_module_demo.py[line:28] WARNING warning message
Thu, 02 Jun 2022 15 :31:35 logging_module_demo.py[line:29] ERROR error message
Thu, 02 Jun 2022 15 :31:35 logging_module_demo.py[line:30] CRITICAL critical message
"""