import pytest
from selenium.webdriver.common.by import By
from ..pages.authentification import AuthPage


def test1_username_field_is_displayed(web_driver):
    auth_page = AuthPage(web_driver)
    auth_page.open_login()
    assert auth_page.username_field_is_displayed()


def test2_password_field_is_displayed(web_driver):
    auth_page = AuthPage(web_driver)
    auth_page.open_login()
    assert auth_page.password_field_is_displayed()


def test3_submit_button_is_clickable(web_driver):
    auth_page = AuthPage(web_driver)
    auth_page.open_login()
    assert auth_page.submit_button_is_clickable()


def test4_checkbox_remember_me_is_clickable(web_driver):
    auth_page = AuthPage(web_driver)
    auth_page.open_login()
    assert auth_page.checkbox_remember_me_is_clickable()


@pytest.mark.parametrize('checkbox', [True, False])
def test5_login_fields_filling(web_driver, checkbox):
    auth_page = AuthPage(web_driver)
    auth_page.open_login()
    email_field = auth_page.username_field
    email_field.clear()
    email_field.send_keys('ps_tanusha@mail.ru')
    passw_field = auth_page.password_field
    passw_field.send_keys('ps_tanusha')
    checkbox_field = auth_page.checkbox_remember_me
    if checkbox is True:
        checkbox_field.click()
    else:
        pass
    web_driver.find_element(By.XPATH, '//span[@class="elementor-button-text"]').click()
    result = web_driver.find_element(By.XPATH, '//label[@class="error"]')
    assert result.text != "Hm... that username and/or password didn't work."


def test6_login_success(web_driver):
    auth_page = AuthPage(web_driver)
    auth_page.open_login()
    auth_page.username_field.send_keys('ps_tanusha@mail.ru')
    auth_page.password_field.send_keys('ps_tanusha')
    auth_page.submit_button.click()
    assert auth_page.greeting_text() == "Welcome to Goodbudget! We're glad you're here."
