class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.LoggedIn_As_xpath="//*[@id='logout-form']/div[2]/label/preceding-sibling::*[1]"
        self.Log_Out_button_xpath="/html//input[@id='logout-form:logout']"

    def click_log_out_button(self):
        self.driver.find_element_by_xpath(self.Log_Out_button_xpath).click()

    def check_logout_button_display(self):
        bool = self.driver.find_element_by_xpath(self.Log_Out_button_xpath).is_displayed()
        return bool




