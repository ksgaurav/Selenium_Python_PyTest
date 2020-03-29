from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import re

from selenium.webdriver.support.wait import WebDriverWait


class SignUpPage():
    global regex
    regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    def __init__(self, driver):
        self.driver = driver
        self.signup_page_dialogue = "//*[@id='content-main']/h1"
        # self.first_name_textbox = "//*[@id='signup:fname']"
        self.firstname_textbox_id = "signup:fname"
        self.lastname_textbox = "//*[@id='signup:lname']"
        self.lastname_textbox_name = "signup:lname"
        self.email_box = "//*[@id='signup:email']"
        self.mailing_address = "/html//input[@id='signup:street']"
        self.city_textbox = "//*[@id='signup:city']"
        self.city_locator_id = "signup:city"
        self.state_dropdown = "//*[@id='signup:state']"
        self.postalcode = "//*[@id='signup:zip']"
        self.postal_code_css_loc = "input#signup:zip"
        self.password_textbox = "//*[@id='signup:password']"
        self.birth_Date = "//*[@id='BirthDate']"
        self.form_submit_button = "//*[@id='signup:signup']"
        self.firstname_mandatory_dialogue = "//*[@id='signup:fname']/following-sibling::*[1]"
        self.lastName_mandatory_dialogue = "//*[@id='signup:lname']/following-sibling::*[1]"
        self.email_mandatory_dialogue = "//*[@id='signup:email']/following-sibling::*[1]"
        self.mailing_address_dialogue = "//*[@id='signup:street']/following-sibling::*[1]"
        self.city_mandatory_dialogue = "//*[@id='signup:city']/following-sibling::*[1]"
        self.state_mandatory_dialogue = "//*[@id='signup:state']/following-sibling::*[1]"
        self.postalCode_mandatory_dialogue = "//*[@id='signup:zip']/following-sibling::*[1]"
        self.password_mandatory_dialogue = "//*[@id='signup:password']/following-sibling::*[1]"
        self.successfull_signUp = "//*[@id='content-main']/h1"

    def signUp_page_displayed(self):
        signup = self.driver.find_element_by_xpath(self.signup_page_dialogue).text
        return signup

    # Here we will locate by id
    def enter_firstName(self, firstname):
        # self.driver.find_element_by_xpath(self.first_name_textbox).send_keys(firstname)
        self.driver.find_element_by_id(self.firstname_textbox_id).send_keys(firstname)

    # Here we will locate by name
    def enter_lastName(self, lastName):
        # self.driver.find_element_by_xpath(self.lastname_textbox).send_keys(lastName)
        self.driver.find_element_by_name(self.lastname_textbox_name).send_keys(lastName)

    def enter_email(self, email):
        # self.check_email_regEx(self, email)
        self.driver.find_element_by_xpath(self.email_box).send_keys(email)

    def enter_mailing_address(self, mailingaddress):
        self.driver.find_element_by_xpath(self.mailing_address).send_keys(mailingaddress)

    # Using DOM to locate
    def enter_city(self, city):
        # self.driver.document.get_element_by_id(self.city_locator_id).send_keys(city)
        self.driver.find_element_by_xpath(self.city_textbox).send_keys(city)

    def select_state(self, state):
        dropdown = self.driver.find_element_by_xpath(self.state_dropdown)
        dd = Select(dropdown)
        dd.select_by_visible_text(state)

    # using cssSelector to locate
    def enter_postal_code(self, postalCode):
        self.driver.find_element_by_xpath(self.postalcode).send_keys(postalCode)
        # self.driver.find_element_by_css_selector(self.postal_code_css_loc).send_keys(postalCode)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(password)

    # Implementing explicit Wait for button to be present
    def click_on_form_submit_button(self):
        # wait = WebDriverWait(self.driver, 15)
        # wait.until(expected_conditions.visibility_of_element_located_by_xpath(self.form_submit_button))
        self.driver.find_element_by_xpath(self.form_submit_button).click()

    def enter_birth_date(self, date):
        self.driver.find_element_by_xpath(self.birth_Date).send_keys(date)

    def validate_signup_successfull(self):
        signup_successfull = self.driver.find_element_by_xpath(self.successfull_signUp).text
        return signup_successfull

    def firstName_mandatory_dialogue(self):
        fdialogue = self.driver.find_element_by_xpath(self.firstname_mandatory_dialogue).text
        return fdialogue

    def lastName_mandat_dialogue(self):
        lMandDialogue = self.driver.find_element_by_xpath(self.lastName_mandatory_dialogue).text
        return lMandDialogue

    def email_mandat_dialogue(self):
        emailDialogue = self.driver.find_element_by_xpath(self.email_mandatory_dialogue).text
        return emailDialogue

    def mailing_address_mandat_dialogue(self):
        addressDialogue = self.driver.find_element_by_xpath(self.mailing_address_dialogue).text
        return addressDialogue

    def city_mand_dialogue(self):
        cityDialogue = self.driver.find_element_by_xpath(self.city_mandatory_dialogue).text
        return cityDialogue

    def state_mandat_dialogue(self):
        stateDialogue = self.driver.find_element_by_xpath(self.state_mandatory_dialogue).text
        return stateDialogue

    def postal_code_mandat_dialogue(self):
        postalCodeDialogue = self.driver.find_element_by_xpath(self.postalCode_mandatory_dialogue).text
        return postalCodeDialogue

    def password_mandat_dialogue(self):
        pwdMandatDialogue = self.driver.find_element_by_xpath(self.password_mandatory_dialogue).text
        return pwdMandatDialogue

    def check_email_regEx(self, email):
        if re.search(regex, email, flags=0):
            print("Valid Email")
        else:
            print("Invalid Email")
