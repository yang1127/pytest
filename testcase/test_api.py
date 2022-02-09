import requests

from common.yaml_util import YamlUtil


class TestRequests(object):

    # access_token = ""

    # get请求：获取接口统一鉴权码taken接口
    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid": "wx74a8627810cfa308",
            "secret": "e40a02f9d79a8097df497e6aaf93ab80"
        }
        # res = requests.get(url=url, params=data)
        res = requests.request(method="get", url=url, params=data)
        print(res.json())

        # TestRequests.access_token = res.json()['access_token']
        YamlUtil().write_extract_yaml({'access_token': res.json()['access_token']})

    # post请求：编辑便签
    def test_edit_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token="
        value = YamlUtil().read_extract_yaml('access_token')
        print(value)
        data = {
            "tag": {
                "id": 134,
                "name": "广东人"
            }
        }
        # res = requests.post(url=url, json=data)  # 为嵌套字典时，用json
        res = requests.request(method="post", url=url, json=data)
        print(res.json())



    '''
    # 文件上传
    def test_file_uoload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" + TestRequests.access_token
        data = {
            "media": open(r"/Users/yangzhiqi/Desktop", "rb")
        }
        res = requests.request("post", url=url, json=data)
        print(res.json())
    '''


'''
if __name__ == '__main__':
    TestRequests().test_get_token()
    TestRequests().test_edit_flag()
    # TestRequests().test_file_uoload()
'''
