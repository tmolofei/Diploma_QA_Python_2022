from selenium.webdriver.common.by import By
from .base_page import BasePage


user_name_field = (By.ID, 'username')
password_field = (By.ID, 'password')
checkbox_remember_me = (By.XPATH, '//span[@class="elementor-field-option"]')
submit_button = (By.XPATH, '//span[@class="elementor-button-text"]')
greeting_message = (By.XPATH, '//*[@id="summary"]/div/div/p')


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_login(self):
        self.driver.get('https://goodbudget.com/login')

    @property
    def username_field(self):
        return self.find_element(user_name_field)

    def username_field_is_displayed(self):
        return self.username_field.is_displayed()

    @property
    def password_field(self):
        return self.find_element(password_field)

    def password_field_is_displayed(self):
        return self.password_field.is_displayed()

    @property
    def checkbox_remember_me(self):
        return self.find_element(checkbox_remember_me)

    def checkbox_remember_me_is_clickable(self):
        return self.checkbox_remember_me.is_enabled()

    @property
    def submit_button(self):
        return self.find_element(submit_button)

    def submit_button_is_clickable(self):
        return self.submit_button.is_enabled()

    def greeting_text(self):
        return self.find_element(greeting_message).text
