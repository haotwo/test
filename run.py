#作者:HP
#日期:2020-04-15 23:25
#文件:run

import unittest
import HTMLTestReportCN
from tools.test_http_request import TestHttpRequest
from tools.project_path import *
suite=unittest.TestSuite()
loader=unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))    #测试类实例

#执行用例
with open(test_report_path,'wb') as file:
    runner=HTMLTestReportCN.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title="接口单元测试报告",
                                           description="接口自动化报告",
                                           tester='Lyle')
    runner.run(suite)


