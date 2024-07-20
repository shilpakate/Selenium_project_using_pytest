import time
import pytest
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.customlogger import logger


class TestLoginPage:
    base_url = ReadConfig().get_base_url()
    username = ReadConfig().get_username()
    password = ReadConfig().get_password()

    def test_page_title(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(3)

        pg_title = self.driver.title

        if pg_title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot("screenshots\\" + "login_page_title.png")
            assert False

    def test_login(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(2)

        # Login POM
        login_obj = LoginPage(self.driver)
        login_obj.set_user_name(self.username)
        login_obj.set_password(self.password)
        login_obj.click_login_button()

        time.sleep(2)

        pg_title = self.driver.title

        if pg_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot("screenshots\\" + "login_page_error.png")
            assert False
