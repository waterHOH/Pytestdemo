import pytest, time, csv, requests, json

from conmon.requests_util import RequestsUtil
from conmon.yaml_util import YamlUtil


class TestLogin1:

    # 这个setup_class 在所有用例之前都执行一次
    def setup_class(self):
        print("\n在每个类执行的初始化的工作：例如：创建日志的对象，创建数据库的链接，创建接口的请求对象")

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml("get_token.yml"))
    def test_binglinchengxia_01(self, caseinfo):
        print("测试名称", caseinfo["name"])
        print("测试地址", caseinfo["request"]["url"])
        print("测试请求", caseinfo["request"]["data"])
        print("测试头部", caseinfo["request"]["headers"])
        print("测试断言", caseinfo["validate"])
        url = caseinfo["request"]["url"]
        body = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        # 发起post请求，获取返回的数据
        r = requests.post(url, headers=headers, json=body)
        # print(r.text)
        # 测试请求状态
        if r.status_code == 200 and r.json()["s"] == 1:
            print(r.json()["a"]["hd1051"])
        else:
            print("报错提示：", r.json()["a"]["system"]["error"]["msg"], "\n具体信息：",
                  r.json()["a"]["system"]["error"]["from"])

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml("edit_flag.yml"))
    def test_binglinchengxia_02(self, caseinfo):
        print("测试名称", caseinfo["name"])
        print("测试地址", caseinfo["request"]["url"])
        print("测试请求", caseinfo["request"]["data"])
        print("测试头部", caseinfo["request"]["headers"])
        print("测试断言", caseinfo["validate"])
        dq = csv.reader(open(r'D:\Desktop\jemter\预上线\组队三人.csv', 'r'))
        for jcs in dq:
            list1 = list(jcs)
            sevid = list1[0]
            uid = list1[1]
            url = caseinfo["request"]["url"] + "sevid=" + sevid + "&uid=" + uid + ""
            body = caseinfo["request"]["data"]
            headers = caseinfo["request"]["headers"]
            # 发起post请求，获取返回的数据
            r = requests.post(url, headers=headers, json=body)
            # print(r.text)
            # 测试请求状态
            if r.status_code == 200 and r.json()["s"] == 1:
                print(r.json()["a"]["hd1051"])
            else:
                print("报错提示：", r.json()["a"]["system"]["error"]["msg"], "\n具体信息：",
                      r.json()["a"]["system"]["error"]["from"])

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml("edit_flag.yml"))
    def test_binglinchengxia_03(self, caseinfo):
        print("测试名称", caseinfo["name"])
        print("请求方式", caseinfo["request"]["method"])
        print("测试地址", caseinfo["request"]["url"])
        print("请求信息", caseinfo["request"]["data"])
        print("测试头部", caseinfo["request"]["headers"])
        print("测试断言", caseinfo["validate"])
        url = caseinfo["request"]["url"]
        body = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        method = caseinfo["request"]["method"]
        # r = requests.post(url, headers=headers, json=body)
        # 通过conmmon里的request_util.py文件里的RequestsUtil类里send_request函数，发起请求
        RequestsUtil().send_request(method, url, body, headers)

    # 在每个用例之前执行一次
    def setup(self):
        print('\n在执行测试用例之前执行的代码')

    # @pytest.fixture(scope="作用域", pa0rams="数据驱动", attouse="自动执行", ids="自定义参数名", name="重命名")
    def test_03_baili(self, conn_database):
        dq = csv.reader(open(r'D:\Desktop\jemter\预上线\组队三人.csv', 'r'))
        for jcs in dq:
            list1 = list(jcs)
            sevid = list1[0]
            uid = list1[1]
            url2 = 'http://lyjxtime.tuziyouxi.com/'
            # url2 = 'http://lyjxydcsf2.hnyoulu.com/'
            body = {"season": {"greExpect": {}}}
            body = {"item": {"useforhero": {"count": 1, "heroid": 1, "id": 11}}}
            headers = {'content-type': "application/json"}
            # 发起post请求，获取返回的数据
            r = requests.post(url2 + 'cmd_t.php?json=1&tpass=abcddd123&sevid=' + str(sevid) + '&uid=' + str(uid),
                              headers=headers, json=body)
            print(sevid, uid, r.status_code, (json.loads(r.text))['s'])
            # 数据写入exttract.yaml文件
            YamlUtil().write_exttract_yaml({sevid: uid})
            # 断言验证请求状态和游戏内请求状态是否响应正常
            assert r.status_code == 200 and (json.loads(r.text))['s'] == 1
            # assert "item" in r.json()

    # @pytest.mark.skipif(age <= 18, reason="年龄小于18跳过")  # 有条件跳过
    def test_04_baili(self):
        # 读取exttract.yaml里的数据
        uid = YamlUtil().read_exttract_yaml("17")
        print(uid)

    def teardown(self):
        print('在执行测试用例之后的扫尾的代码')

    def tear_down_class(self):
        print('\n在每个类执行完之后的扫尾工作：比如：销毁日志对象，销毁数据库连接，销毁接口的请求对象')

# if __name__ == '__main__':
#     pytest.main(["-vs"])
#     # pytest.main(["-vs", "-n=2"])  # 两个线程执行用例m
#     # pytest.main(['-vs', '--html=./report/report1.html'])  # 输出html报告
#     # pytest.main(["-vs", "--reruns=2"])  # 失败重跑2次
#     # pytest.main(["-m", "smoke"])  # 执行有smoke装饰的测试用例
#     # pytest.main(["-m", "smoke1 or smoke2"]) # 执行有smoke1或者smoke2装饰的测试用例
