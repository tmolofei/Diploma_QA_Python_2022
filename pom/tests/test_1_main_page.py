from pom.pages.main_page import MainPage


def test1_log_in_is_displayed(web_driver):
    main_page = MainPage(web_driver)
    main_page.open()
    assert main_page.login_button_is_displayed()


def test2_sign_up_form_is_displayed(web_driver):
    main_page = MainPage(web_driver)
    main_page.open()
    assert main_page.signup_button_is_displayed()


def test3_open_log_in_form(web_driver):
    main_page = MainPage(web_driver)
    main_page.open()
    assert main_page.login_button_is_clickable()


def test3_sign_up_form_is_displayed(web_driver):
    main_page = MainPage(web_driver)
    main_page.open()
    assert main_page.signup_button_is_displayed()


def test4_open_sign_up_form(web_driver):
    main_page = MainPage(web_driver)
    main_page.open()
    assert main_page.signup_button_is_clickable()
