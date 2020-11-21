import pytest
import time
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from utilities.read_Properties import ReadConfig
from utilities.custom_Logger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.click_on_customers_menu()
        self.addcust.click_on_customers_menu_item()
        time.sleep(2)
        self.addcust.click_on_add_new()
        time.sleep(2)
        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.set_email(self.email)
        self.addcust.set_password("test123")
        self.addcust.set_customer_roles("Guests")
        self.addcust.set_manager_of_vendor("Vendor 2")
        self.addcust.set_gender("Male")
        self.addcust.set_first_name("Amit")
        self.addcust.set_last_name("Singh")
        self.addcust.set_dob("07/21/1991")  # Format: D / MM / YYY
        self.addcust.set_company_name("XYZ_ABC")
        self.addcust.set_admin_content("This is for testing.........")
        self.addcust.click_on_save()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

