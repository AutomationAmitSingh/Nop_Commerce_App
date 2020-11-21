import time
import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilities.read_Properties import ReadConfig
from utilities.custom_Logger import LogGen


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.click_on_customers_menu()
        self.addcust.click_on_customers_menu_item()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        #searchcust.set_email("victoria_victoria@nopCommerce.com")
        searchcust.set_email("james_pan@nopCommerce.com")
        time.sleep(5)
        searchcust.click_search()
        time.sleep(5)
        status = searchcust.search_customer_by_email("james_pan@nopCommerce.com")
        print(status)
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")

