#作者:HP
#日期:2020-04-16 22:01
#文件:get_cookie
from tools.project_path import *
import pandas as pd
class GetData:
    Cookie=None
    load_id=None
    NoRegTel=pd.read_excel(test_case_path,sheet_name='init').iloc[0,0]
    normal_tel=pd.read_excel(test_case_path,sheet_name='init').iloc[1,0]
    admin_tel=pd.read_excel(test_case_path,sheet_name='init').iloc[2,0]
    loan_member_id=pd.read_excel(test_case_path,sheet_name='init').iloc[3,0]
    memberId=pd.read_excel(test_case_path,sheet_name='init').iloc[4,0]



print(GetData.loan_member_id)