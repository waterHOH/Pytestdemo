import requests, json


class RequestsUtil:
    # 类变量：通过类名访问
    session = requests.session()

    def send_request(self, method, url, data, headers, **kwargs):
        method = str(method).lower()
        req = None
        if method == "get":
            rep = RequestsUtil.session.request(method=method, url=url, params=data, headers=headers, **kwargs)
        else:
            # data = json.dumps(data)
            rep = RequestsUtil.session.request(method=method, url=url, data=data, headers=headers, **kwargs)

        # rep = RequestsUtil.session.request(method=method, url=url, data=data, headers=headers, **kwargs)

        # 测试请求状态
        if rep.status_code == 200 and rep.json()["s"] == 1:
            print(rep.json()["a"]["hd1051"])
        else:
            print("报错提示：", rep.json()["a"]["system"]["error"]["msg"], "\n具体信息：",
                  rep.json()["a"]["system"]["error"]["from"])
        return rep.text
