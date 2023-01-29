import pytest, time, csv, requests, json


class TestLogin:
    age = 18

    # # 这个setup_class 在所有用例之前都执行一次
    # def setup_class(self):
    #     print("\n在每个类执行的初始化的工作：例如：创建日志的对象，创建数据库的链接，创建接口的请求对象")
    #
    # # 在每个用例之前执行一次
    # def setup(self):
    #     print('\n在执行测试用例之前执行的代码')

    def test_00_qingcicuanren(self):
        print('\n在执行青瓷传人测试用例')
        a = 1
        quality_1 = 0
        quality_2 = 0
        quality_3 = 0
        quality_4 = 0
        quality_5 = 0
        run_num = 0
        while a <= 1:
            a = a + 1
            # 循环读取表中的数据
            # dq = csv.reader(open(r'D:\Desktop\jemter\预上线\招兵买马.csv', 'r'))
            # dq = csv.reader(open(r'/游动/Excel/岳麓书院.csv', 'r'))
            dq = csv.reader(open(r'C:\Users\root\PycharmProjects\untitled\游动\Excel/单人.csv', 'r'))
            for jcs in dq:
                list1 = list(jcs)
                sevid = list1[0]
                uid = list1[1]
                url2 = 'http://lyjxtime.tuziyouxi.com/'
                # url2 = 'http://lyjxydcsf2.hnyoulu.com/'
                headers = {'content-type': "application/json"}

                # 进入活动
                body = {"hd1036": {"enter": {}}}
                r = requests.post(url2 + 'cmd_t.php?json=1&tpass=abcddd123&sevid=' + str(sevid) + '&uid=' + str(uid),
                                  headers=headers, json=body)
                try:
                    cm = (json.loads(r.text))["a"]["hd1036"]["my"]["cm"]
                except:
                    print("异常输出")

                # 集市购买
                body_shop = {"shop": {"shopGift": {"id": 2}}}
                r = requests.post(url2 + 'cmd_t.php?json=1&tpass=abcddd123&sevid=' + str(sevid) + '&uid=' + str(uid),
                                  headers=headers, json=body_shop)
                # 使用静心玉恢复选拔次数
                body_recovery = {"hd1036": {"recovery": {"count": 1000}}}
                r = requests.post(url2 + 'cmd_t.php?json=1&tpass=abcddd123&sevid=' + str(sevid) + '&uid=' + str(uid),
                                  headers=headers, json=body_recovery)

                # 升级匠作处
                Yx = 0
                while Yx <= 25:
                    body_upgradeYx = {"hd1036": {"upgradeYx": {}}}
                    r = requests.post(
                        url2 + 'cmd_t.php?json=1&tpass=abcddd123&sevid=' + str(sevid) + '&uid=' + str(uid),
                        headers=headers, json=body_upgradeYx)
                    Yx = Yx + 1
                # 升级场门
                upgradeCm = 0
                while upgradeCm <= 5:
                    body_upgradeCm = {"hd1036": {"upgradeCm": {}}}
                    r = requests.post(
                        url2 + 'cmd_t.php?json=1&tpass=abcddd123&sevid=' + str(sevid) + '&uid=' + str(uid),
                        headers=headers, json=body_upgradeCm)
                    upgradeCm = upgradeCm + 1
                # 升级学习建筑
                upgradeYf = 1
                while upgradeYf < 6:
                    Yf1 = 1
                    while Yf1 < 60:
                        body_upgradeYf = {"hd1036": {"upgradeYf": {"id": upgradeYf}}}
                        r = requests.post(
                            url2 + 'cmd_t.php?json=1&tpass=abcddd123&sevid=' + str(sevid) + '&uid=' + str(uid),
                            headers=headers, json=body_upgradeYf)
                        Yf1 = Yf1 + 1
                    upgradeYf = upgradeYf + 1
                # 选拔
                recruit = 1
                while recruit < 10:
                    body_recruit = {"hd1036": {"recruit": {}}}
                    r_recruit = requests.post(
                        url2 + 'cmd_t.php?json=1&tpass=abcddd123&sevid=' + str(sevid) + '&uid=' + str(uid),
                        headers=headers, json=body_recruit)
                    print(r_recruit.text)

                    json.loads(r_recruit.text)
                    # 获取请求返回状态的值
                    try:
                        Request_return_status = r_recruit.json()["s"]
                    except:
                        print("异常输出")
                    # 校验请求状态
                    if Request_return_status == 0:
                        print("区服:", list1[0], "uid:", list1[1], "选拔失败",
                              (json.loads(r_recruit.text))['a']['system']['error']['msg'])
                    else:
                        # 　quality品质
                        len1 = len((json.loads(r_recruit.text))['a']['hd1036']['recruit'])
                        # print(len1)
                        len2 = 0

                        while len2 < len1:
                            quality = (json.loads(r_recruit.text))['a']['hd1036']['recruit'][int(len2)]['quality']
                            # print(quality)

                            if quality == 1:
                                quality_1 = quality_1 + 1
                            elif quality == 2:
                                quality_2 = quality_2 + 1
                            elif quality == 3:
                                quality_3 = quality_3 + 1
                            elif quality == 4:
                                quality_4 = quality_4 + 1
                            elif quality == 5:
                                quality_5 = quality_5 + 1
                                # 招募品种为5的工匠
                                recruit_id = (json.loads(r_recruit.text))['a']['hd1036']['recruit'][int(len2)]['id']
                                recruit_name = (json.loads(r_recruit.text))['a']['hd1036']['recruit'][int(len2)]['name']
                                e1 = (json.loads(r_recruit.text))['a']['hd1036']['recruit'][int(len2)]['eps']['e1']
                                e2 = (json.loads(r_recruit.text))['a']['hd1036']['recruit'][int(len2)]['eps']['e2']
                                e3 = (json.loads(r_recruit.text))['a']['hd1036']['recruit'][int(len2)]['eps']['e3']
                                e4 = (json.loads(r_recruit.text))['a']['hd1036']['recruit'][int(len2)]['eps']['e4']
                                e5 = (json.loads(r_recruit.text))['a']['hd1036']['recruit'][int(len2)]['eps']['e5']
                                body_recruitTrue = {"hd1036": {"recruitTrue": {"id": recruit_id}}}
                                r_recruitTrue = requests.post(
                                    url2 + 'cmd_t.php?json=1&tpass=abcddd123&sevid=' + str(sevid) + '&uid=' + str(uid),
                                    headers=headers, json=body_recruitTrue)
                                print(uid, "招募了：", recruit_name, "属性：", e1, e2, e3, e4, e5)
                            len2 = len2 + 1
                            run_num = run_num + 1
                    recruit = recruit + 1
                    # print(run_num)

        else:

            print("当前匠门等级：", cm, "一共选拔：", run_num, "工匠")
            print("品质1:", quality_1, "品质2:", quality_2, "品质3:", quality_3, "品质4:", quality_4, "品质5:", quality_5)
            print("品质1概率:", quality_1 / run_num, "\n品质2概率:", quality_2 / run_num, "\n品质3概率:", quality_3 / run_num,
                  "\n品质4概率:",
                  quality_4 / run_num, "\n品质5概率:", quality_5 / run_num)
            print('执行完毕')

    @pytest.mark.run(order=2)  # 标记第2个执行
    def test_01_baili(self):
        print('测试百里1')

    @pytest.mark.run(order=1)  # 标记第1个执行
    def test_02_baili(self):
        # assert 1 == 2
        print('测试百里2')

    @pytest.mark.skip(reason="跳过说明")  # 无条件跳过
    # @pytest.mark.smoke
    def test_03_baili(self):
        print('冒烟测试')

    @pytest.mark.skipif(age <= 18, reason="年龄小于18跳过")  # 有条件跳过
    def test_04_baili(self):
        print('测试百里4')

    # def teardown(self):
    #      print('在执行测试用例之后的扫尾的代码')

    # def tear_down_class(self):
    #     print('\n在每个类执行完之后的扫尾工作：比如：销毁日志对象，销毁数据库连接，销毁接口的请求对象')


if __name__ == '__main__':
    # pytest.main(["-vs", "-n=2"])  # 两个线程执行用例m
    pytest.main(['-vs', '--html=./report/report10.html'])  # 输出html报告
    # pytest.main(["-vs", "--reruns=2"])  # 失败重跑2次
    # pytest.main(["-m", "smoke"])  # 执行有smoke装饰的测试用例
    # pytest.main(["-m", "smoke1 or smoke2"]) # 执行有smoke1或者smoke2装饰的测试用例
