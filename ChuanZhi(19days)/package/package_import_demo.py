# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/23 14:11
# IDE:        PyCharm
# Title:      package_import_demo.py
# import
# 方法一
"""
1.导入
    import 包名.模块名
2.调用功能
    包名.模块名.功能()
"""
# 需求：导入mypackage包下的模块1，使用这个模块内的info_print1函数
import mypackage.my_module1
mypackage.my_module1.info_print1()


# 方法二: 注意 设置__init__.py 文件里面的all列表，添加的是允许导入的模块  --__all__ = ['my_module1', 'my_module2']
"""
1.导入
    from 包名 import *
2.调用功能
    模块名.功能()
"""
from mypackage import *
my_module2.info_print2()
# my_module1.info_print1()    # 如果all只允许my_module2可以导入，那么使用my_module1就会报错：NameError: name 'my_module1' is not defined
