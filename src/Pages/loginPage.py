from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_xpath = "/html//input[@id='login-form:email']"
        self.password_textbox_xpath = "//input[@id='login-form:password']"
        self.submit_button = "/html//input[@id='login-form:login']"
        self.blank_login_email_dialogue = "//*[@id='login-messages']/table/tbody/tr[1]/td"
        self.blank_login_password_dialogue = "//*[@id='login-messages']/table/tbody/tr[2]/td"
        self.blank_only_pass_dialogue = "//*[@id='login-messages']/table/tbody/tr/td"
        self.invalid_wrong_credential_dialogue = "//*[@id='login-messages']/table/tbody/tr/td"
        self.signUp_button = "//*[@id='login-form:signup']"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.submit_button).click()

    def check_blank_email_credentials(self):
        email_value = self.driver.find_element_by_xpath(self.blank_login_email_dialogue).text
        return email_value

    def check_blank_Password_credentials(self):
        pass_Value = self.driver.find_element_by_xpath(self.blank_login_password_dialogue).text
        return pass_Value

    def check_blank_only_pass_credential(self):
        pass_value = self.driver.find_element_by_xpath(self.blank_only_pass_dialogue).text
        return pass_value

    def check_invalid_credential_dialogue(self):
        wrong_credent = self.driver.find_element_by_xpath(self.invalid_wrong_credential_dialogue).text
        return wrong_credent

    def click_on_signup_button(self):
        self.driver.find_element_by_xpath(self.signUp_button).click()

    def signUp_button_present(self):
        signup_button = self.driver.find_element_by_xpath(self.signUp_button).is_displayed()
        return signup_button

    def wait_for_element(self):
        element = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located_by_id(self.signUp_button))
