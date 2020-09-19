# -*- coding: utf-8 -*- 
import os, sys, platform

# 找到当前目录
project_root = os.path.dirname(os.path.realpath(__file__))
print(project_root)

# 不同的系统，使用不同的命令语句

if platform.system() == 'Linux':
    command = sys.executable + ' -m pip freeze > ' + project_root + '/requirements.txt'
if platform.system() == 'Windows':
    command = '"' + sys.exec_prefix + '\Scripts\pip" freeze > ' + project_root + '\\requirements.txt'
    # command = '"' + sys.exec_prefix + '\Scripts\pipreqs" . --encoding=utf-8 --force '

# # 拼接生成requirements命令s
print(command)
#
# # 执行命令。
os.system(command)
download_command = '"' + sys.exec_prefix + '\Scripts\pip" ' + 'download -d ' + project_root + '\packages -r requirements.txt -i https://pypi.doubanio.com/simple'
print(download_command)
os.system(download_command)
