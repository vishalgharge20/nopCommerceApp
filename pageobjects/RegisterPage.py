from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class RegisterPage:
    checkbox_male_id = 'gender-male'
    checkbox_female_id = 'gender-female'
    textbox_firstname_id = 'FirstName'
    textbox_lastname_id = 'LastName'
    day_DOB_css = "select[name='DateOfBirthDay']"
    month_DOB_css = "select[name='DateOfBirthMonth']"
    year_DOB_css = "select[name='DateOfBirthYear']"
    textbox_email_id = 'Email'
    checkbox_newsletter_id = 'Newsletter'
    textbox_password_id = 'Password'
    textbox_confirmpassword_id = 'ConfirmPassword'
    button_register_id = 'register-button'

    def __init__(self, driver):
        self.driver = driver

    def tick_male_option(self):
        self.driver.find_element(By.ID, self.checkbox_male_id).click()

    def tick_female_option(self):
        self.driver.find_element(By.ID, self.checkbox_female_id).click()

    def set_first_name(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).clear()
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).clear()
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def set_dob(self,day,month,year):
        wait = WebDriverWait(self.driver, 10)

        dropdown_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.day_DOB_css)))
        dropdown_element.click()
        dropdown_day = Select(self.driver.find_element(By.CSS_SELECTOR,self.day_DOB_css))
        dropdown_day.select_by_visible_text(day)

        dropdown_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.month_DOB_css)))
        dropdown_element.click()
        dropdown_month = Select(self.driver.find_element(By.CSS_SELECTOR,self.month_DOB_css))
        dropdown_month.select_by_visible_text(month)

        dropdown_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.month_DOB_css)))
        dropdown_element.click()
        dropdown_year = Select(self.driver.find_element(By.CSS_SELECTOR,self.year_DOB_css))
        dropdown_year.select_by_visible_text(year)

    def set_email(self,email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def tick_newsletter(self):
        self.driver.find_element(By.ID, self.checkbox_newsletter_id).click()

    def set_password(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def confirm_password(self,confirm_password):
        self.driver.find_element(By.ID, self.textbox_confirmpassword_id).clear()
        self.driver.find_element(By.ID, self.textbox_confirmpassword_id).send_keys(confirm_password)

    def click_register(self):
        self.driver.find_element(By.ID, self.button_register_id).click()




