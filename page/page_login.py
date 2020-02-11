"""登录页面封装"""
import page
from base.base import Base


class PageLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.page_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.page_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, code):
        self.base_input(page.page_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.page_login_btn)

    #获取登录失败的文本信息
    def page_get_error_info(self):
        return self.base_get_text(page.page_login_error_info)

    #点击 错误信息 确定按钮
    def page_click_confirm(self):
        self.base_click(page.page_login_error_confirm)



    # 登录业务组合方法
    def page_login(self, username, pwd, code):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()
