# from pom.pages.base_page import BasePage
# from selenium.webdriver.common.by import By
#
# login_field = (By.ID, 'j_username')
# pass_field = (By.NAME, 'j_password')
# submit_button = (By.NAME, 'Submit')
# greeting_message = (By.XPATH, '//*[@id="summary"]/div/div/p')
#
#
# class LoginPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     def open(self):
#         self.driver.get('https://goodbudget.com/')
#
#     def log_in(self, user, password):
#         self.find_element(login_field).send_keys(user)
#         self.find_element(pass_field).send_keys(password)
#         self.find_element(submit_button).click()
