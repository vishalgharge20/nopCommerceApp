from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    button_login_xpath = '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button'
    link_logout_xpath = '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a'
    login_link_xpath = "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def click_login_link(self):
        self.driver.find_element(By.XPATH,self.login_link_xpath).click()