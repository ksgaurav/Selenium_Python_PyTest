from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.Pages.signUpPage import SignUpPage
from src.Pages.loginPage import LoginPage
import unittest


class LoginTest(unittest.TestCase):
    global siteurl
    siteurl = "http://demo.borland.com/InsuranceWebExtJS/index.jsf"

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox(
            executable_path="C:/Users/GauravSingh/PycharmProjects/SeleniumProject/drivers/geckodriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    # validate that SIGNUP button is present on the screen
    def test_signUp_button_present(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)  # creating instance of Login page to access all it's functions
        expected = login.signUp_button_present()
        assert expected == True

    # validate that clicking on SIGNUP button should open SIGNUP form
    def test_signup_form_present(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)
        login.click_on_signup_button()
        signup_page = SignUpPage(driver)
        expected = signup_page.signUp_page_displayed()
        assert expected == "Create A New Account"

    # Entering All Mandatory Field(not entering optional fields) with non-existing email should successfully SignUp
    def test_mandatory_field(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)
        login.click_on_signup_button()
        signup_page = SignUpPage(driver)
        signup_page.enter_firstName("Mohit")
        signup_page.enter_lastName("Singh")
        signup_page.enter_email("moit2win@gmail.com")
        signup_page.enter_mailing_address("Society1")
        signup_page.enter_city("Windsor")
        signup_page.select_state("Connecticut")
        signup_page.enter_postal_code("90001")
        signup_page.enter_password("ABC@123")
        signup_page.click_on_form_submit_button()
        signup_page = SignUpPage(driver)
        expected = signup_page.validate_signup_successfull()
        assert expected == "Thank you for signup!"

    # Entering All Field(mandatory & Optional) should successfully Signup
    def test_all_field_happy_Path(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)
        login.click_on_signup_button()
        signup_page = SignUpPage(driver)
        signup_page.enter_firstName("Mark")
        signup_page.enter_lastName("Zuckerberg")
        signup_page.enter_birth_date("17/03/2020")
        signup_page.enter_email("mzuhkehhz@gmail.com")
        signup_page.enter_mailing_address("Facebook")
        signup_page.enter_city("Windsor")
        signup_page.select_state("Connecticut")
        signup_page.enter_postal_code("90001")
        signup_page.enter_password("ABC@123")
        signup_page.click_on_form_submit_button()
        expected = signup_page.validate_signup_successfull()
        assert expected == "Thank you for signup!"

    def test_all_field_existing_email(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)
        login.click_on_signup_button()
        signup_page = SignUpPage(driver)
        signup_page.enter_firstName("Mark")
        signup_page.enter_lastName("Zuckerberg")
        signup_page.enter_birth_date("17/03/2020")
        signup_page.enter_email("mzuckerberg@gmail.com")
        signup_page.enter_mailing_address("Facebook")
        signup_page.enter_city("Windsor")
        signup_page.select_state("Connecticut")
        signup_page.enter_postal_code("90001")
        signup_page.enter_password("ABC@123")
        signup_page.click_on_form_submit_button()
        email_duplicate_message = signup_page.email_mandat_dialogue()
        assert email_duplicate_message == "Email is already registered"

    # Not entering value in any field and click on submit should throw required field message
    def test_all_blank_submit(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)
        login.click_on_signup_button()
        signup_page = SignUpPage(driver)
        signup_page.click_on_form_submit_button()
        expected_messgae_firstname_Required = signup_page.firstName_mandatory_dialogue()
        assert expected_messgae_firstname_Required == "required"
        expected_messgae_lastname_required = signup_page.lastName_mandat_dialogue()
        assert expected_messgae_lastname_required == "required"
        expected_message_email_required = signup_page.email_mandat_dialogue()
        assert expected_message_email_required == "required"
        expected_message_address = signup_page.mailing_address_mandat_dialogue()
        assert expected_message_address == "required"
        expected_message_city_required = signup_page.city_mand_dialogue()
        assert expected_message_city_required == "required"
        expected_message_State_Required = signup_page.state_mandat_dialogue()
        assert expected_message_State_Required == "required"
        expected_postalcode_message = signup_page.postal_code_mandat_dialogue()
        assert expected_postalcode_message == "required"
        expected_message_password = signup_page.password_mandat_dialogue()
        assert expected_message_password == "required"

    # Validate that entering all fields except FirstName should throw message for mandatory field
    def test_all_but_firstName(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)
        login.click_on_signup_button()
        signup_page = SignUpPage(driver)
        signup_page.enter_lastName("Zucker")
        signup_page.enter_birth_date("17/03/2020")
        signup_page.enter_email("mzuckberg@gmail.com")
        signup_page.enter_mailing_address("Facebook")
        signup_page.enter_city("Windsor")
        signup_page.select_state("Connecticut")
        signup_page.enter_postal_code("90001")
        signup_page.enter_password("ABC@123")
        signup_page.click_on_form_submit_button()
        expected_messgae_firstName_Required = signup_page.firstName_mandatory_dialogue()
        assert expected_messgae_firstName_Required == "required"

    # Validate that entering all fields except lastName should throw message for last Name required
    def test_all_but_lastName(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)
        login.click_on_signup_button()
        signup_page = SignUpPage(driver)
        signup_page.enter_firstName("Mark")
        signup_page.enter_birth_date("17/03/2020")
        signup_page.enter_email("mzbe7gg@gmail.com")
        signup_page.enter_mailing_address("Facebook")
        signup_page.enter_city("Windsor")
        signup_page.select_state("Connecticut")
        signup_page.enter_postal_code("90001")
        signup_page.enter_password("ABC@123")
        signup_page.click_on_form_submit_button()
        expected_messgae_lastName_Required = signup_page.lastName_mandat_dialogue()
        assert expected_messgae_lastName_Required == "required"

    def test_all_but_email(self):
        driver = self.driver
        driver.get(siteurl)
        login = LoginPage(driver)
        login.click_on_signup_button()
        signup_page = SignUpPage(driver)
        signup_page.enter_firstName("Mark")
        signup_page.enter_lastName("Zuckerberg")
        signup_page.enter_birth_date("17/03/2020")
        signup_page.enter_mailing_address("Facebook")
        signup_page.enter_city("Windsor")
        signup_page.select_state("Connecticut")
        signup_page.enter_postal_code("90001")
        signup_page.enter_password("ABC@123")
        signup_page.click_on_form_submit_button()
        expected_message_email_required = signup_page.email_mandat_dialogue()
        assert expected_message_email_required == "required"


@classmethod
def tearDownClass(cls) -> None:
    # cls.driver.close()
    print("Test Completed")
