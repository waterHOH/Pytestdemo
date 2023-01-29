import pytest

# 函数级别部分前置
from conmon.yaml_util import YamlUtil


@pytest.fixture(scope="function")
def conn_database():
    print("链接数据库")
    yield  # yield和return一样是表示返回数据的意思，区别在于yield返回多次以及多个数据，return只会返回一次，return之后不能接代码
    print("关闭数据库")


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_exttract_yaml()
