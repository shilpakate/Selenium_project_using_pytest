from selenium.webdriver.common.by import By


class SearchCustomer:
    email_id = "SearchEmail"
    first_name_id = "SearchFirstName"
    last_name_id = "SearchLastName"
    search_button_id = "search-customers"
    company_name_id = "SearchCompany"

    # table xpath
    search_result_table_xpath = '//table[@id="customers-grid"]'
    table_xpath = '//table[@id="customers-grid"]'
    table_row_xpath = '//table[@id="customers-grid"]/tbody/tr'
    table_column_xpath = '//table[@id="customers-grid"]//tbody/tr[1]/td'

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def set_first_name(self, f_name):
        self.driver.find_element(By.ID, self.first_name_id).clear()
        self.driver.find_element(By.ID, self.first_name_id).send_keys(f_name)

    def set_last_name(self, l_name):
        self.driver.find_element(By.ID, self.last_name_id).clear()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(l_name)

    def set_company_name(self, company_name):
        self.driver.find_element(By.ID, self.company_name_id).clear()
        self.driver.find_element(By.ID, self.company_name_id).send_keys(company_name)

    def search_button(self):
        self.driver.find_element(By.ID, self.search_button_id).click()

    def get_number_of_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))

    def get_number_of_columns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column_xpath))

    def search_by_email(self, email):
        flag = False
        for r in range(1, self.get_number_of_rows() + 1):
            table_email_data_xpath = '//table[@id="customers-grid"]//tbody/tr[{}]/td[2]'.format(r)
            table_email = self.driver.find_element(By.XPATH, table_email_data_xpath).text
            if email == table_email:
                flag = True
        return flag

    def search_by_name(self, s_name):
        flag = False
        for r in range(1, self.get_number_of_rows() + 1):
            table_s_name_data_xpath = '//table[@id="customers-grid"]//tbody/tr[{}]/td[3]'.format(r)
            table_name = self.driver.find_element(By.XPATH, table_s_name_data_xpath).text
            if s_name == table_name:
                flag = True
        return flag

    def search_by_company_name(self, c_name):
        flag = False
        for r in range(1, self.get_number_of_rows() + 1):
            table_cname_xpath = '//table[@id="customers-grid"]//tbody/tr[{}]/td[5]'.format(r)
            table_cname = self.driver.find_element(By.XPATH, table_cname_xpath).text
            if c_name == table_cname:
                flag = True
        return flag

    def search_by_company_name_and_email(self,email, c_name):
        flag = False
        for r in range(1, self.get_number_of_rows() + 1):
            table_email_xpath = '//table[@id="customers-grid"]//tbody/tr[{}]/td[2]'.format(r)
            table_email = self.driver.find_element(By.XPATH, table_email_xpath).text
            table_cname_xpath = '//table[@id="customers-grid"]//tbody/tr[{}]/td[5]'.format(r)
            table_cname = self.driver.find_element(By.XPATH, table_cname_xpath).text
            if email == table_email and c_name == table_cname :
                flag = True
            return flag

