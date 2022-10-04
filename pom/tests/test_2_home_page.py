import csv
from time import sleep
from datetime import date
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pom.pages.home_page import HomePage


current_date = date.today().strftime('%m/%d/%Y')
NEW_PAYEE = 'Gazprom'
AMOUNT_SUM_BEFORE_ADDING = 47300.00
NEW_AMOUNT = 500.00
ELEMENTS_COUNT = 8
NEW_NAME_OF_TRANSACTION = 'MartinFood'
NOTES_FOR_TRANSACTION = 'AbrakadabrA'


def test1_logout_button_is_displayed(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    assert home_page.log_out_button_is_clickable()


def test2_accounts_button_is_clickable(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    assert home_page.accounts_button_is_clickable()


def test3_envelopes_button_is_clickable(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.account_button.click()
    assert home_page.envelopes_button_is_clickable()


def test4_add_transaction_button_is_clickable(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    assert home_page.add_transaction_button_is_clickable()


def test5_added_new_transaction(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.add_new_transaction()
    home_page.added_date().clear()
    home_page.added_date().send_keys(current_date)
    payee_value = home_page.payee_field_info()
    payee_value.send_keys(NEW_PAYEE)
    amount_value = home_page.new_amount_info()
    amount_value.send_keys(NEW_AMOUNT)
    Select(home_page.new_envelope_field()).select_by_index(3)
    home_page.save_button().click()
    result = home_page.added_new_payee()
    assert NEW_AMOUNT, NEW_PAYEE in result.text


def test6_total_amount_after_added_transaction(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    sleep(3)
    amount_sum_after_adding = home_page.total_amount_sum()
    amount_sum_after_adding = float(amount_sum_after_adding.text.replace(",", ""))
    assert amount_sum_after_adding == (AMOUNT_SUM_BEFORE_ADDING - NEW_AMOUNT)


def test7_delete_button_is_clickable(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.payee_one_checkbox_find().click()
    sleep(2)
    assert home_page.delete_button_is_clickable()


def test8_selected_transaction(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.all_checkbox_find().click()
    sleep(5)
    elements = web_driver.find_elements(By.XPATH, '//tr[@class="selected"]')
    assert int(len(elements)) == (ELEMENTS_COUNT + 1)


def test9_delete_one_transaction(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.payee_one_checkbox_find().click()
    home_page.payee_delete.click()
    web_driver.find_element(By.ID, 'bulkEditDeleteSave').click()
    home_page.all_checkbox_find().click()
    elements = web_driver.find_elements(By.XPATH, '//tr[@class="selected"]')
    assert int(len(elements)) == ELEMENTS_COUNT


def test10_search_field_is_displayed(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    assert home_page.found_search_field().is_displayed()


def test11_search_button_is_clickable(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    assert home_page.search_button_is_clickable().is_enabled()


@pytest.mark.parametrize('values', ['Medicine', 'Food', 'Gaz', 'Clothes', 'Cafe'])
def test12_the_search_result(web_driver, values):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.found_search_field().send_keys(values)
    home_page.search_button_is_clickable().click()
    result = web_driver.find_elements(By.XPATH, '//*[@id="transactions-tbody"]/tr[2]/th[2]')
    for filter_items in result:
        # filter_items.text
        assert values in filter_items.text


def test13_change_name_transaction(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.payee_one_checkbox_find().click()
    home_page.change_name_button().click()
    home_page.new_name_field().send_keys(NEW_NAME_OF_TRANSACTION)
    home_page.confirm_name_button().click()
    sleep(1)
    home_page.found_search_field().send_keys(NEW_NAME_OF_TRANSACTION)
    home_page.search_button_is_clickable().click()
    result = web_driver.find_element(By.XPATH, '//*[@id="transactions-tbody"]/tr[2]/th[2]')
    assert NEW_NAME_OF_TRANSACTION in result.text


def test14_add_notes(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.payee_one_checkbox_find().click()
    home_page.add_notes_button().click()
    home_page.notes_field().send_keys(NOTES_FOR_TRANSACTION)
    home_page.notes_confirm().click()
    result = home_page.added_notes().get_attribute('data-content')
    assert NOTES_FOR_TRANSACTION == result


def test15_add_edit_button_is_clickable(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    assert home_page.add_or_edit_button().is_enabled()


def test16_change_budget(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.add_or_edit_button().click()
    home_page.budget_fields().clear()
    home_page.budget_fields().send_keys(600.00)
    home_page.save_changes().click()
    result = home_page.new_budget().text
    assert 600.00 == float(result)


def test17_change_budget(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.status_checkboxes().click()
    result = home_page.change_status_checkboxes().get_attribute('title')
    assert result == 'Cleared'


def test18_accounts_button_is_switched_to(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.account_button.click()
    result = home_page.account_is_swithed_to().text
    assert 'My Account' in result


def test19_export_csv_button_is_clickable(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    assert home_page.export_csv_button().is_enabled()


def test20_csv_is_downloaded(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.export_csv_button().click()
    sleep(1)
    with open('/home/tm/Downloads/history.csv', newline='') as file:
        reader = csv.reader(file)
        info_from_file = []
        for row in reader:
            info_from_file.append(row[1])
    assert 'Food' in info_from_file


def test21_logout_is_successful(web_driver):
    home_page = HomePage(web_driver)
    home_page.open()
    home_page.log_out_button.click()
    assert home_page.good_bye_text() == "You've been successfully logged out"
