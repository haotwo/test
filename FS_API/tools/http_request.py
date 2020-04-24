# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2020/4/16 9:38
#文件 :http_request.py


import requests

class HttpRequest:    #创建一个http请求

    def http_request(self,url,data,http_method,cookie=None):
        try:
            if http_method.upper()=="GET":
                res=requests.get(url,data,cookies=cookie)

            elif http_method.upper()=="POST":
                res=requests.post(url,data,cookies=cookie)

            else:
                print("请求方式错误")
        except Exception as e:
            print("请求方式错误：{0}".format(e))
            raise e

        return res    #返回结果

# if __name__ == '__main__':
#     #登录
#     login_url="http://47.107.168.87:56478/futureloan/mvc/api/member/login"
#     login_data={"mobilephone":"15307186393","pwd":"123456"}
#     login_res=HttpRequest().http_request(login_url,login_data,'post')
#     print(login_res.json())