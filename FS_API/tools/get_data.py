# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2020/4/17 9:45
#文件 :get_cookie.py
from tools.project_path import *
import pandas as pd
class GetData:
    Cookie=None
    NoRegName=pd.read_excel(case_path,sheet_name='init').iloc[0,0]
    # print(NoRegName)