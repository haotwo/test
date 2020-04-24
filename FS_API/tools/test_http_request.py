# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2020/4/16 18:11
#文件 :test_http_request.py
import unittest
from tools.http_request import HttpRequest
from tools.do_excel import DoExcel
from ddt import ddt,data
from tools.get_data import GetData
from tools.project_path import *

test_data=DoExcel().get_data(case_path)      #测试数据获取文件

@ddt    #进行数据分离
class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        pass
    @data(*test_data)
    def test_api(self,item):
        print("测试开始：{0}".format(item['title']))    #测试标题
        res=HttpRequest().http_request(item['url'],eval(item['data']),item['http_method'],getattr(GetData,'Cookie'))    #获取请求
        if res.cookies:    #利用反射获取cookies
            setattr(GetData,'Cookie',res.cookies)
        try:    #进行断言
            self.assertEqual(str(item['expect']),res.json()['code'])
            TestResult='PASS'
        except Exception as e:
            TestResult='Failed'
            print("执行用例出错:{}".format(e))
            raise e
        finally:     #将测试结果返回文档中
            DoExcel().write_back(case_path,item['sheet_name'],item['case_id']+1,str(res.json()),TestResult)
    def tearDown(self):
        pass

