#作者:HP
#日期:2020-04-20 21:00
#文件:test_http_request

import unittest
from tools.http_request import HttpRequest
from ddt import ddt,data   #列表
from  tools.do_excel import DoExcel
from tools.project_path import *
from tools.my_log import MyLog
from tools.do_mysql import DoMysql
from tools.get_data import GetData
test_data=DoExcel.get_data(test_case_path)
my_logger=MyLog()
@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self,item):
        #请求之前完成loan_id的替换
        if item['data'].find('${loan_id}')!=-1:
            if getattr(GetData,'load_id')==None:
                query_sql='select Id from loan where Member ID={0}'.format(getattr(GetData,'loan_member_id'))
                loan_id=DoMysql().do_mysql(query_sql)[0][0]
                item['data']=item['data'].replace('${loan_id}',str(loan_id))
                setattr(GetData,'load_id',loan_id)   #利用反射存储结果
            else:
                item['data'] = item['data'].replace('${loan_id}', str(getattr(GetData,'loan_id')))

        res=HttpRequest.http_request(item['url'],eval(item['data']),item['http_method'],getattr(GetData,'Cookie'))
        if res.cookies:
            setattr(GetData,'Cookie',res.cookies)
        try:
            self.assertEqual(str(item['expected']),res.json()['code'])
            TestResult='PASS'
        except AssertionError as e:
            TestResult = 'Failed'
            my_logger.info('执行用列出错：{0}'.format(e))
            raise e
        finally:
            DoExcel.write_back(test_case_path,item['sheet_name'],item['case_id']+1,str(res.json()),TestResult)
            my_logger.error("获取到的结果是：{0}".format(res.json()))

        # print(res.json())
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()