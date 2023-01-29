import pytest


class TestLogin:
    # 　@pytest.mark.smoke1
    def test_01_xingyao(self):
        print('冒烟测试2')


if __name__ == '__main__':
    pytest.main(["-vs"])
