import os
import yaml


class YamlUtil:
    # 读取extract.yml文件
    def read_exttract_yaml(self, key):
        # 打开extract.yml文件
        with open(os.getcwd() + "/extract.yml", mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key];

    # 写入extract.yml文件
    def write_exttract_yaml(self, data):
        # 打开extract.yml文件
        with open(os.getcwd() + "/extract.yml", mode="a", encoding="utf-8") as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除extract.yml文件
    def clear_exttract_yaml(self):
        # 打开extract.yml文件
        with open(os.getcwd() + "/extract.yml", mode="w", encoding="utf-8") as f:
            f.truncate()

    # 读取测试用例的gat_token.yml文件
    def read_testcase_yaml(self, yaml_name):
        # 打开extract.yml文件
        # with open(os.getcwd() + "/test_youdong/" + yaml_name, mode="r", encoding="utf-8") as f:
        #     value = yaml.load(stream=f, Loader=yaml.FullLoader)
        #     return value;
        with open(os.getcwd() + './'+yaml_name, mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value;
