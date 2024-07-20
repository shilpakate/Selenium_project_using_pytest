import pytest
import time
from page_objects.login_page import LoginPage
from page_objects.add_customer import AddCustomer
from page_objects.search_customer_page import SearchCustomer
from utilities.read_properties import ReadConfig


class TestSearchCustomerByEmailAndCompanyName:
    base_url = ReadConfig().get_base_url()
    username = ReadConfig().get_username()
    password = ReadConfig().get_password()

    @pytest.mark.search
    def test_search_customer_usising_companyname(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(3)

        # login page obj
        self.login_obj = LoginPage(self.driver)
        self.login_obj.set_user_name(self.username)
        self.login_obj.set_password(self.password)
        self.login_obj.click_login_button()
        time.sleep(3)

        # click customer menu
        self.customer_obj = AddCustomer(self.driver)
        self.customer_obj.click_customer_menu()
        time.sleep(2)
        self.customer_obj.click_customer_menu_item()
        time.sleep(3)

        # search email
        self.search_obj = SearchCustomer(self.driver)
        self.search_obj.set_company_name("Indian Cricket Team")
        self.search_obj.search_button()
        time.sleep(2)

        # read data from table
        response = self.search_obj.search_by_company_name("Indian Cricket Team")

        assert True == response
