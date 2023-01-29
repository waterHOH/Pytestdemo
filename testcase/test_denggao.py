# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import json
import os
import csv
import time
import pytest

from pyparsing import common

dq = csv.reader(open(r'C:\Users\root\PycharmProjects\Pytestdemo/Test_csv/1-20.csv', 'r'))

# pytest框架的py文件名必须以test_开头或者_test结尾
# pytest框架的类名必要要以Test开头
# pytest框架的测试用例必须以test_开头
class TestHt:
    def test_changetime(self):
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
            print(sevid, uid, r.status_code)


if __name__ == '__main__':
    pytest.main(["-vs"])
