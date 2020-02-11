from selenium import webdriver
from time import sleep


class GetDriver():
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        # 判断driver为空
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get("http://127.0.0.1")
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(30)
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        #判断driver不为空，关闭
        if cls.driver:
            sleep(3)
            cls.driver.quit()
            cls.driver=None  #一定要置空

if __name__ == '__main__':
    GetDriver.get_driver()

