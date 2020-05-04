#作者:HP
#日期:2020-04-27 21:26
#文件:do_mysql

import pymysql
from tools.project_path import *
from tools.read_config import ReadConfig
from tools.get_data import GetData
class DoMysql:
    #关键字参数的传递
    def do_mysql(self,query_sql,state='all'):
        db_config=eval(ReadConfig.get_config(case_config_path,'DB','db_config')) #从配置文件获取db
        #创建一个数据库连接
        cnn=pymysql.connect(**db_config)

        #游标cursor
        cursor=cnn.cursor()
        #执行语句
        cursor.execute(query_sql)
        if state==1:
            res=cursor.fetchone()
        else:
            res=cursor.fetchall()

        #关闭游标
        cursor.close()
        #关闭数据库
        cnn.close()

        return  res
# if __name__ == '__main__':
#     query_sql='select max(Id) from loan where MemberID={0}'.format(getattr(GetData,'loan_member_id'))
#     res=DoMysql().do_mysql(query_sql)
#     print(res)