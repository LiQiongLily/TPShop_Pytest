from selenium.webdriver.common.by import By

"""以下为登录 配置信息"""

# 首页 登录链接
page_login_link = By.LINK_TEXT, "登录"
# 输入用户名
page_username = By.ID, "username"
# 密码
page_pwd = By.ID, "password"
# 验证码
page_code = By.ID, "verify_code"
# 登录按钮
page_login_btn = By.NAME, "sbtbutton"

#错误信息文本
page_login_error_info=By.CLASS_NAME,"layui-layer-content"

#错误的文本信息  确定按钮
page_login_error_confirm=By.LINK_TEXT,"确定"


#登录成功获取 昵称
page_login_success= By.CLASS_NAME,"userinfo"

# 点击 首页
page_login_index=By.LINK_TEXT,"首页"

#登录成功后，安全退出
page_login_safe_exists=By.LINK_TEXT,"安全退出"