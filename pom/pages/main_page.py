from pom.pages.base_page import BasePage
from .locators import main_page_locators as loc


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://goodbudget.com/')

    def open_login_form(self):
        self.find_element(loc.log_in_button).click()

    @property
    def login_button(self):
        return self.find_element(loc.sign_up_button)

    def login_button_is_displayed(self):
        return self.login_button.is_displayed()

    def login_button_is_clickable(self):
        return self.login_button.is_enabled()

    @property
    def signup_button(self):
        return self.find_element(loc.sign_up_button)

    def signup_button_is_displayed(self):
        return self.signup_button.is_displayed()

    def signup_button_is_clickable(self):
        return self.signup_button.is_enabled()
