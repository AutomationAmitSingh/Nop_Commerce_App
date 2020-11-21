import pytest
from pageObjects.loginPage import LoginPage
from utilities.read_Properties import ReadConfig
from utilities.custom_Logger import LogGen
from utilities import XL_Utils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.get_application_url()
    path = ReadConfig.get_login_data_path()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XL_Utils.get_row_count(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XL_Utils.read_data(self.path, 'Sheet1', r, 1)
            self.password = XL_Utils.read_data(self.path, 'Sheet1', r, 2)
            self.exp = XL_Utils.read_data(self.path, 'Sheet1', r, 3)
            print("User name & Password for row : "+str(r) + " is "+self.user + " & " + self.password)
            self.lp.set_user_name(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            act_title = self.driver.title
            print(act_title)
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.click_logout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    self.lp.click_logout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")

