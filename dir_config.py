#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2020/6/27 23:00
#@Author    :Lyle
#@File      :dir_config.py
import os

#获取当前文件路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

screenshot_dir=os.path.join(project_path,"Outputs","screenshots")

# print(project_path)


