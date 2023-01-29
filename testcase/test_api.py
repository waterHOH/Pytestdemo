import pytest


class TestApi:

    @pytest.mark.parametrize("args", ["测试1", "测试2", "测试3"])
    def test_api1(self, args):
        print(args)

    # 一个参数对应一个值
    @pytest.mark.parametrize("name,age", [["测试1", 11], ["测试2", 22], ["测试3", 33]])
    def test_api2(self, name, age):
        print(name, age)


if __name__ == '__main__':
    pytest.main(["-vs", "test_api.py"])
