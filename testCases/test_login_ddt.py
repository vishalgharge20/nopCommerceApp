import time
import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilis


class Test_002_DDT_Login:
    baseUrl_login = ReadConfig.GetApplicationUrl()
    path = ".\\TestData\\login_testdata.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.ddt
    def test_login_ddt(self,setup):
        self.driver = setup
        self.logger.info("********** Test_002_Login_ddt **********")
        self.logger.info("********** test_login Started **********")
        self.driver.get(self.baseUrl_login)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtilis.getRowCount(self.path,'Sheet1')
        print("Number of rows in Excel:",self.rows)

        list_status = []  # Empty list variable

        for r in range(2,self.rows+1):
            self.user = XLUtilis.readData(self.path,'Sheet1',r,1)
            self.password = XLUtilis.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtilis.readData(self.path,"Sheet1",r,3)

            self.lp.set_user_name(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "nopCommerce demo store"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("********** Test Passed ***********")
                    self.lp.click_logout()
                    self.lp.click_login_link()
                    list_status.append("Pass")

                elif self.exp == "Fail":
                    self.logger.info("********** Test Failed ***********")
                    screenshot_name = "test_login_ddt_fail_" + str(r - 1) + ".png"
                    self.driver.save_screenshot(".\\Screenshot\\"+screenshot_name)
                    self.lp.click_logout()
                    self.lp.click_login_link()
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("********** Test Failed ***********")
                    screenshot_name = "test_login_ddt_fail_" + str(r - 1) + ".png"
                    self.driver.save_screenshot(".\\Screenshot\\" + screenshot_name)
                    self.lp.click_logout()
                    self.lp.click_login_link()
                    list_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("********** Test Passed ***********")
                    self.lp.click_logout()
                    self.lp.click_login_link()
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("********* Login DDT Test passed")
            assert True
        else:
            self.logger.info("********* Login DDT Test Failed")
            assert False

        self.logger.info("******** Login DDT Finished *********")
        self.driver.close()


















