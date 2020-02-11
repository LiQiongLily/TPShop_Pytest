import sys
import os
sys.path.append(os.getcwd())


import pytest
import yaml
from page.page_title import PageTitle
from page.page_index import PageIndex
from page.page_login import PageLogin
from tool.get_driver import GetDriver



def get_data():
    with open("./data/login_data.yaml", "r", encoding="utf-8")as f:
        d = yaml.load(f)
        arr = []
        for data in d.values():
            arr.append((data.get("username"),
                        data.get("pwd"),
                        data.get("code"),
                        data.get("success"),
                        data.get("expect")))

    return arr


class TestLogin():
    driver=None
    # 初始化
    
    def setup_class(self):
        self.driver = GetDriver.get_driver()

        # 获取PageIndex对象
        self.index = PageIndex()
        # 获取PageLogin对象
        self.login = PageLogin()
        # 获取PageTitle对象
        self.title = PageTitle()
        #点击 登录 链接
        self.index.page_login_link()

    # 结束,退出driver

    def teardown_class(self):
        GetDriver.quit_driver()

        # 测试方法
    @pytest.mark.parametrize("username,pwd,code,success,expect",get_data())
    def test_login(self, username, pwd, code,success,expect):

        self.login.page_login(username, pwd, code)
        #成功的用例
        if success:
            msg = self.title.page_get_nickname()
            print("获取的昵称为：", msg)
            #退出登录
            self.title.page_exists()
            #点击登录链接
            self.index.page_login_link()

            try:

                assert expect in msg
            except Exception as e:
                #获取截图
                self.login.base_get_img()
                raise e
        #失败用例
        else:
            error_text = self.login.page_get_error_info()
            print("错误信息为：",error_text)
            #点击错误信息的 确定按钮
            self.login.page_click_confirm()

            try:
                assert expect in error_text
            except Exception as e:
                #获取 截图
                self.login.base_get_img()

