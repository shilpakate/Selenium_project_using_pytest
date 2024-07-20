import time
import pytest
from page_objects.login_page import LoginPage
from utilities import xl_utils
from utilities.read_properties import ReadConfig

credentials = ([xl_utils.read_data(row_num=2, col_num=1), xl_utils.read_data(row_num=2, col_num=2),
                xl_utils.read_data(row_num=2, col_num=3), 2],
               [xl_utils.read_data(row_num=3, col_num=1), xl_utils.read_data(row_num=3, col_num=2),
                xl_utils.read_data(row_num=3, col_num=3), 3],
               [xl_utils.read_data(row_num=4, col_num=1), xl_utils.read_data(row_num=4, col_num=2),
                xl_utils.read_data(row_num=4, col_num=3), 4])


class TestDdtLoginPage:
    base_url = ReadConfig().get_base_url()

    @pytest.mark.parametrize("xl_username, xl_password, xl_result, row_n", credentials)
    def test_ddt_login_page(self, set_up, xl_username, xl_password,
                            xl_result, row_n):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(3)

        # login page obj
        login_obj = LoginPage(self.driver)
        login_obj.set_user_name(xl_username)
        login_obj.set_password(xl_password)
        login_obj.click_login_button()

        time.sleep(3)

        pg_title = self.driver.title

        if pg_title == xl_result:
            xl_utils.write_data(row_num=row_n, col_num=4, data="Passed")
            assert True
        else:
            xl_utils.write_data(row_num=row_n, col_num=4, data="Failed")
            assert False
