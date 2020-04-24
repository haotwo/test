# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2020/4/21 9:31
#文件 :read_congig.py
import configparser

class ReadConfig:

    @staticmethod
    def get_config(file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path)

        return cf [section][option]

# if __name__ == '__main__':
#     from tools.project_path import *
#     print(ReadConfig.get_config(config_path,'MODE','mode'))

