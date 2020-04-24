# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2020/4/21 9:09
#文件 :project_path.py
import os


#获取文件的位置
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试用例路径
case_path=os.path.join(project_path,'test_data','test_data.xlsx')

#测试报告路径
report_path=os.path.join(project_path,'test_result','html_report','test_result.html')

#配置文件路径
config_path=os.path.join(project_path,'conf','case.config')
