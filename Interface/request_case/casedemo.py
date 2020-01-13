
import json

import os
import requests


class SET:
    def __init__(self):
        # 通过登陆获取token

       r=requests.post(
                url='http://192.168.1.145:9000/api/sys/common/login',
                data={"username":"admin","password":"123456"}
               )
        #把token写入到文件中
       with open(self.base_dir(),'w') as f:
           f.write(r.text)

    def base_dir(self):
        '''读取当前文件的目录'''
        return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/config/','token.md')
         # print(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/config/','token.md'))

    def get_token(self):

        with open(self.base_dir(),'r') as f:
            # return f.read()
            print(f.read())

        # 定义一个post传递参数的方法
    def test_post(self, url="http://150.223.10.116:83/service/user"):
        # 将data转换为json格式
        data = "{ \"deptId\":234, \"deptName\": \"测试部门29\", \"email\": \"monsterxxx@163.com\", \"mobile\": 18000000000, \"name\": \"11XX29\"," \
            " \"password\": \"123123123\", \"roleIds\": [ 1 ], \"status\": 1, \"userId\":0 , \"userIdCreate\": 1, \"username\": 100}"
        r2 = requests.post(
            headers={
                "token": self.token,
                "Content-Type": "application/json"},
            # 使用contenttype才能将body传递至参数
            url=url, data=data.encode("utf-8"))  # 编辑date字符格式
        result1 = json.loads(r2.text)
        result = json.loads(r2.text)['msg']  # 获取相应信息
        # reid=json.loads(r2.text)['data']['rows']['userId']#获取相应信息
        print(result1)
        print(result)
        # print(reid)
        # return result


    def test_ppp(self, url, data):
        # data=json.loads(data)
        r = requests.post(url=url,data=data)
        self.result = r.json()
        result = self.result['message']
        return result

    # self.assertEqual(self.result['message'], 'event id already exists')

    # 定义一个get获取信息的方法
    def test_get(self, url, params={}):
        url = "http://150.223.10.116:83/aqpx/people"
        # 将token参数放入params参数中
        params["token"] = self.token
        r3 = requests.get(url, params).text
        result1 = json.loads(r3)
        result = json.loads(r3)['msg']  # 获取相应信息
        print(result1)
        print(result)
        return result


    # 定义一个put修改信息的方法
    # 修改部门
    def test_put(self, data, num):
        # 将data转换为json格式
        data = "{ \"delFlag\": 0, \"deptId\": 0, \"name\": \"string\", \"orderNum\": 0, \"parentId\": 0, \"remake\": \"修改\"}"
        url2 = "http://150.223.10.116:83/service/dept/" + str(num)
        print(url2)
        r2 = requests.put(
            headers={"token": self.token, "Content-Type": "application/json"},
            url=url2, data=data.encode("utf-8"))
        result1 = json.loads(r2.text)
        result = json.loads(r2.text)['msg']
        print(result1)
        print(result)


    # 定义一个删除的方法
    def test_delete(self, url, num):
        pass

    # 定义一个上传文件的方法
    def test_send_files(self):
        pass


if __name__ == '__main__':
   set = SET()
   print(set.get_token())