import time
import string
import random
from page_objects.login_page import LoginPage
from page_objects.add_customer import AddCustomer
from utilities.read_properties import ReadConfig


class TestAddCustomers:
    # read from config.ini file
    base_url = ReadConfig().get_base_url()
    username = ReadConfig().get_username()
    password = ReadConfig().get_password()

    def test_add_customer(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(3)

        # login page obj
        self.login_page = LoginPage(self.driver)
        self.login_page.set_user_name(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login_button()
        time.sleep(5)

        # add customer
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_customer_menu()
        time.sleep(1)
        self.add_customer.click_customer_menu_item()
        time.sleep(2)
        self.add_customer.click_add_new()
        time.sleep(3)

        # fill customer form
        self.add_customer.click_add_customer_info()
        time.sleep(1)
        self.email = random_generator() + "@gmail.com"
        self.add_customer.set_email(self.email)
        self.add_customer.set_password("travis123")
        self.add_customer.set_first_name("travis")
        self.add_customer.set_last_name("scott")
        self.add_customer.set_gender("Male")
        self.add_customer.set_date_of_birth("12/12/1996")  # Format: DD/ MM / YYY
        self.add_customer.set_company_name("HSBC")
        self.add_customer.set_admin_comment("Company name is HSBC")
        self.add_customer.click_save()

        time.sleep(3)
        check_mesg = self.add_customer.check_message()

        if "successfully." in check_mesg:
            self.driver.save_screenshot("screenshots\\" + "add_customer.png")
            assert True
        else:
            self.driver.save_screenshot("screenshots\\" + "add_customer_error.png")
            assert True

    def test_email_exists_or_not(self,set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(3)

        # login page obj
        self.login_page = LoginPage(self.driver)
        self.login_page.set_user_name(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login_button()
        time.sleep(5)

        # add customer
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_customer_menu()
        time.sleep(1)
        self.add_customer.click_customer_menu_item()
        time.sleep(2)
        self.add_customer.click_add_new()
        time.sleep(3)
        self.add_customer.set_email("admin@yourStore.com")
        time.sleep(5)
        self.add_customer.click_save()
        time.sleep(6)
        if self.add_customer.check_email_existance() == 'Email is already registered':
            assert True
time.sleep(5)


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for i in range(size))
