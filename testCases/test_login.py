import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl_login = ReadConfig.GetApplicationUrl()
    username = ReadConfig.GetUsername()
    password = ReadConfig.GetPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self,setup):
        self.driver = setup
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page **********")
        self.driver.get(self.baseUrl_login)
        actual_title = self.driver.title
        if actual_title == "nopCommerce demo store. Login":
            self.logger.info("********** TestCase Passed **********")
            assert True
        else:
            self.logger.info("********** TestCase Failed **********")
            assert False
        self.driver.close()

    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** test_login Started **********")
        self.driver.get(self.baseUrl_login)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        if "Welcome to our store" in self.driver.page_source:
            self.logger.info("********** TestCase Passed **********")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshot\\"+"test_login.png")
            self.driver.close()
            self.logger.info("********** TestCase Failed **********")
            assert False
        self.driver.close()








