# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2020/4/16 9:35
#文件 :run.py


#执行文件

import unittest
from tools.test_http_request import TestHttpRequest
import HTMLTestReportCN
from tools.project_path import *

#加载测试用例
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

#将测试结果返回测试报告中
with open(report_path,"wb") as file:
    runner=HTMLTestReportCN.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title="接口自动化",
                                           description="接口自动化",
                                           tester="Lyle")
    runner.run(suite)

