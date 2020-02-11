"""首页封装"""
import page
from base.base import Base


class PageIndex(Base):
    # 点击登录 链接
    def page_login_link(self):
        self.base_click(page.page_login_link)
