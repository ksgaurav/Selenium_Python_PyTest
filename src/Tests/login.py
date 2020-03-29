from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.Pages.homePage import HomePage
from src.Pages.loginPage import LoginPage
import unittest
import time


class LoginTest(unittest.TestCase):
    global siteurl
    siteurl = "http://demo.borland.com/InsuranceWebExtJS/index.jsf"

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox(
            executable_path="C:/Users/GauravSingh/PycharmProjects/SeleniumProject/drivers/geckodriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    # validate that User should successfully login by valid credentials
    def test_login_valid(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)  # creating instance of Login page to access all it's functions
        login.enter_username("john.smith@gmail.com")
        login.enter_password("john")
        login.click_login_button()
        home = HomePage(driver)
        expected = home.check_logout_button_display()  # Validate that LogOut button is present after successful Login
        assert expected == True
        home.click_log_out_button()

    # validate that when UserName and Password both are blank and clicking on Login button should not login and throw expected dialogue
    def test_login_invalid_bothBlank(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)
        login.click_login_button()
        expected_dialogue1 = login.check_blank_email_credentials()
        assert expected_dialogue1 == "Please enter your e-mail"
        expected_dialogue2 = login.check_blank_Password_credentials()
        assert expected_dialogue2 == "Please enter your password"

    # validate that entering only valid userName and blank password and clicking on login button should not successfully Login
    def test_invalid_pass_blank(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)  # creating instance of Login page to access all it's functions
        login.enter_username("john.smith@gmail.com")
        login.click_login_button()
        expected_dialogues = login.check_blank_only_pass_credential()
        assert expected_dialogues == "Please enter your password"

    # validate that entering blank username but valid password and clicking on Login button should not login successfully
    def test_invalid_usename_blank(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)
        login.enter_password("john")
        login.click_login_button()
        expected_dialogue1 = login.check_blank_email_credentials()
        assert expected_dialogue1 == "Please enter your e-mail"

    # validate that entering valid username but wrong password should not login and throw expected Dialogue
    def test_valid_username_wrong_pass(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)  # creating instance of Login page to access all it's functions
        login.enter_username("john.smith@gmail.com")
        login.enter_password("ABCD")  # this is wrong password
        login.click_login_button()
        expected_dialogue = login.check_invalid_credential_dialogue()
        assert expected_dialogue == "Could not log in user: Internal Error"

    # validate that entering valid username but wrong password should not login and throw expected Dialogue
    def test_valid_pass_wrong_username(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)  # creating instance of Login page to access all it's functions
        login.enter_username("john.abc@gmail.com")  # wrong username which does not exist in system
        login.enter_password("john")  # this is correct password
        login.click_login_button()
        expected_dialogue = login.check_invalid_credential_dialogue()
        assert expected_dialogue == "Non-existing email, please try again."

    # validate that agter entering valid username and password and press ENTER key should work as Login button and user login successfully
    def test_valid_credentials_Press_ENTER_key(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)  # creating instance of Login page to access all it's functions
        login.enter_username("john.smith@gmail.com")
        login.enter_password("john").send_keys(Keys.ENTER)  # Press Enter key
        home = HomePage(driver)
        expected = home.check_logout_button_display()  # Validate that LogOut button is present after successful Login
        assert expected == True
        home.click_log_out_button()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        print("Test Completed")
