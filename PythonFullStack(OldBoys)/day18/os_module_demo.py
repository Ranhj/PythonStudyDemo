# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-30 15:52
# className:  os_module_demo.py
"""
OS模块：
    提供对操作系统进行调用的接口
"""

import os
# 获取当前工作目录，即当前Python脚本工作的目录路径
# os.getcwd()
# print(os.getcwd())  #   D:\Study\python_workspace\PythonStudyDemo\PythonFullStack(OldBoys)\day18

# 改变当前脚本工作目录，相当于shell下cd
# os.chdir(r"D:\Study")
# print(os.getcwd())  # D:\Study

# 返回当前目录(.)
# print(os.curdir)    # .

# 获取当前目录的父目录字符串名(..)
# print(os.pardir)    # ..

# 可生成多层递归目录
# os.makedirs('dirname1/dirname2')
# os.makedirs('abc\\def\\rrr\\hhh\\jjj')  # D:\Study\abc\def\rrr\hhh\jjj

# 删除空文件夹，若目录为空则删除，并递归到上一级目录，如若也为空，则继续删除，以此类推；若文件夹有文件则不会删除
# os.removedirs('abc\\def\\rrr\\hhh\\jjj')

# 生成单级目录；相当于shell中 mkdir dirname
# os.mkdir('dirname001')  # D:\Study\dirname001

# 删除单级目录，若目录不为空则无法删除，相当于shell中 rmdir dirname
# os.rmdir('dirname001')  # 目录下有文件的话会报错 OSError: [WinError 145] 目录不是空的。: 'dirname001'
# os.rmdir('dirname1\\dirname2')  # 只会删除dirname2目录，不管dirname1是否为空都不会删除，区别于removedirs递归删除

# 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# dirs = os.listdir(r'D:\Study\视频教程\老男孩Python')
# print(dirs)  # ['day18-python 全栈开发-基础篇', 'day19-python 全栈开发-基础篇', 'day20-python 全栈开发-基础篇']

# 删除一个文件
# os.remove('dirname001') # 不能删除文件夹
# os.remove(r'D:\Study\dirname1\dirname2\dirname_del.txt')    # 只能删除文件

# 重命名文件/目录  os.rename('oldname', 'newname')
# os.rename(r"D:\Study\dirname1\dirname2\haha", "D:\Study\dirname1\dirname2\huhu")
# os.rename(r"D:\Study\dirname1\dirname2\eiei.abc", "D:\Study\dirname1\dirname2\hei.txt")

# 获取文件/目录信息
# info = os.stat(r'D:\Study\dirname1\dirname2\hei.txt')
# print(info)  # os.stat_result(st_mode=33206, st_ino=1688849860349333, st_dev=915205346, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1653978805, st_mtime=1653978805, st_ctime=1653978805)
# print(info.st_size)  # 文件大小 1

# info2 = os.stat('.\\__init__.py')
# print(info2.st_size)

# 输出操作系统特定的路径分隔符，win下为"\\", Linux下为"/"
# print(os.sep)   # \

# 输出当前平台使用的行终止符，win下为"\r\n", Linux下为"\n"
# print(os.linesep)

# 输出用于分割文件路径的字符串
# print(os.pathsep)   # ;

# 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# print(os.name)  # nt

# 运行shell命令，直接显示
# print(os.system("bash command"))
# os.system('dir')
# print(os.system('pwd'))

# 获取系统环境变量
# print(os.environ)   # environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Sniper\\AppData\\Roaming', 'ASL.LOG': 'Destination=file', 'CLASSPATH': '.;C:\\Program Files\\Java\\jdk1.8.0_171\\lib\\dt.jar;C:\\Program Files\\Java\\jdk1.8.0_171\\lib\\tools.jar;', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-BONQSA3', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Sniper', 'IDEA_INITIAL_DIRECTORY': 'D:\\Desktop', 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk1.8.0_171', 'LOCALAPPDATA': 'C:\\Users\\Sniper\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-BONQSA3', 'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\Sniper\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\Sniper\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Java\\jdk1.8.0_171\\bin;C:\\Program Files\\Java\\jdk1.8.0_171\\jre\\bin;D:\\program_files\\Git\\cmd;D:\\program_files\\Xshell\\;D:\\program_files\\Xftp\\;C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\;C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38\\;C:\\Users\\Sniper\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin;;D:\\program_files\\Fiddler', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 62 Stepping 4, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '3e04', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM COMMUNITY EDITION': 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin;', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'D:\\Study\\python_workspace\\PythonStudyDemo', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\Sniper\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\Sniper\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-BONQSA3', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-BONQSA3', 'USERNAME': 'Sniper', 'USERPROFILE': 'C:\\Users\\Sniper', 'WINDIR': 'C:\\WINDOWS'})

# 返回path规范化的绝对路径
# print(os.path.abspath("dirname1"))  # D:\Study\dirname1
# print(os.path.abspath("./dirname1/dirname2/hei.txt")) # D:\Study\dirname1\dirname2\hei.txt

# 将path分割成目录和文件名二元组返回
# print(os.path.split('./dirname1/dirname2/hei.txt')) # ('./dirname1/dirname2', 'hei.txt')

# 返回path的目录，其实就是os.path.split(path)的第一个元素
# print(os.path.dirname(('./dirname1/dirname2/hei.txt'))) # ./dirname1/dirname2

# 返回path最后的文件名，如果path以 / 或 \ 结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# print(os.path.basename('./dirname1/dirname2/hei.txt'))  # hei.txt

# 如果path存在，返回True；如果path不存在，返回False
# print(os.path.exists('./dirname1/dirname2/hei.txt'))    # False
# print(os.path.exists('D:\Study\dirname1\dirname2\hei.txt')) # True

# 如果path是绝对路径，返回True
# print(os.path.isabs('D:\Study\dirname1\dirname2\hei.txt'))  # True
# print(os.path.isabs('./dirname1/dirname2/hei.txt')) # False

# 如果path是一个存在的文件，返回True；否则返回False
# print(os.path.isfile('D:\Study\dirname1\dirname2\hei.txt')) # True
# print(os.path.isfile(r'D:\ddddd'))  # False

# 如果path是一个存在的目录，则返回True；否则返回False
# print(os.path.isdir('D:\Study\dirname1\dirname2\hei.txt')) # False
# print(os.path.isdir('D:\Study\dirname1\dirname2'))  # True

# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# print(os.path.join('D:\Study\dirname1\dirname2[D:\Study\dirname1\dirname2\huhu]'))

# 返回path所指向的文件或者目录的最后存取时间
# time = os.path.getatime('D:\Study\dirname1\dirname2\hei.txt')
# print(time)   # 1653981474.4654834

# 返回path所指向的文件或者目录的最后修改时间
# time2 = os.path.getmtime('D:\Study\dirname1\dirname2\hei.txt')
# print(time2)    # 1654051284.8470924

