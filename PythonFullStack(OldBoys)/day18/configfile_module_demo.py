# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-06-06 15:17
# className:  configfile_module_demo.py
import configparser
config = configparser.ConfigParser()

# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
# config['bitbucket.org'] = {'User': 'hg'}
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'    # mutates the parser
# topsecret['ForwardX11'] = 'no'
# config['DEFAULT']['ForwardX11'] = 'yes'
#
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)


config.read('example.ini')
# print(config.sections())
# print(config.defaults())
# print(config['bitbucket.org']['User'])
#
# for key in config['bitbucket.org']:
#     print(key)

config.remove_section('topsecret.server.com')
config.write(open('i.cfg', 'w'))

print(config.has_section('topsecret.server.com'))   # False


