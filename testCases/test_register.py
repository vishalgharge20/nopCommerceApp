import pytest
from selenium import webdriver
from pageobjects.RegisterPage import RegisterPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Register:
    baseUrl_register = ReadConfig.GetApplicationRegisterUrl()
    firstname = ReadConfig.GetFirstName()
    lastname = ReadConfig.GetLastName()
    day = ReadConfig.GetDay()
    month = ReadConfig.GetMonth()
    year = ReadConfig.GetYear()
    email = ReadConfig.GetEmail()
    password = ReadConfig.GetPassword()
    confirm_password = ReadConfig.GetConfirm_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register(self,setup):
        self.driver = setup
        self.logger.info("********** Test_001_Register **********")
        self.logger.info("********** test_register Started **********")
        self.driver.get(self.baseUrl_register)
        self.driver.maximize_window()
        self.lp = RegisterPage(self.driver)
        self.lp.tick_male_option()
        self.lp.set_first_name(self.firstname)
        self.lp.set_last_name(self.lastname)
        self.lp.set_dob(self.day,self.month,self.year)
        self.lp.set_email(self.email)
        self.lp.tick_newsletter()
        self.lp.set_password(self.password)
        self.lp.confirm_password(self.confirm_password)
        self.lp.click_register()
        self.driver.implicitly_wait(10)
        if self.driver.page_source == 'Your registration completed':
            self.logger.info("********** Test Passed **********")
            assert True
        else:
            self.logger.info("********** Test Failed **********")
            self.driver.save_screenshot(".\\screenshot\\"+"test_register.png")
            assert False
