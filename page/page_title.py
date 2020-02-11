"""登录成功后页面封装"""
import page
from base.base import Base


class PageTitle(Base):
    #获取登录成功昵称
    def page_get_nickname(self):
        return self.base_get_text(page.page_login_success)

    #点击首页
    def page_click_index(self):
        self.base_click(page.page_login_index)

    # 点击安全退出
    def page_click_safe_exists(self):
        self.base_click(page.page_login_safe_exists)

     #登录成功，退出业务方法
    def page_exists(self):
        self.page_click_index()
        self.page_click_safe_exists()


