from selenium.webdriver.common.by import By
from pom.pages.base_page import BasePage
from .locators import home_page_locators as loc


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://goodbudget.com/login')
        self.driver.find_element(By.ID, 'username').clear()
        self.driver.find_element(By.ID, 'username').send_keys('ps_tanusha@mail.ru')
        self.driver.find_element(By.ID, 'password').send_keys('ps_tanusha')
        self.driver.find_element(By.XPATH, '//span[@class="elementor-button-text"]').click()

    @property
    def add_expenses_button(self):
        return self.find_element(loc.add_expenses_button)

    def add_expenses_button_is_clickable(self):
        return self.add_expenses_button.is_enabled()

    @property
    def log_out_button(self):
        return self.find_element(loc.logout_button)

    def log_out_button_is_clickable(self):
        return self.log_out_button.is_enabled()

    def good_bye_text(self):
        return self.find_element(loc.goodbye_text).text

    @property
    def account_button(self):
        return self.find_element(loc.accounts_button)

    def accounts_button_is_clickable(self):
        return self.account_button.is_enabled()

    @property
    def envelope_button(self):
        return self.find_element(loc.envelopes_button)

    def envelopes_button_is_clickable(self):
        return self.envelope_button.is_enabled()

    @property
    def add_transaction_button(self):
        return self.find_element(loc.addtransaction_button)

    def add_transaction_button_is_clickable(self):
        return self.add_transaction_button.is_enabled()

    def add_new_transaction(self):
        return self.add_transaction_button.click()

    def payee_field_info(self):
        return self.find_element(loc.payee_field)

    def new_amount_info(self):
        return self.find_element(loc.amount_field)

    def save_button(self):
        return self.find_element(loc.save_button)

    def new_envelope_field(self):
        return self.find_elements(loc.envelope_field)

    def added_new_payee(self):
        return self.find_element(loc.added_new_payee_1)

    def added_date(self):
        return self.find_element(loc.date_field)

    def payee_one_checkbox_find(self):
        return self.find_element(loc.payee_checkbox)

    def all_checkbox_find(self):
        return self.find_element(loc.all_checkbox_button)

    @property
    def payee_delete(self):
        return self.find_element(loc.delete_button)

    def delete_button_is_clickable(self):
        return self.payee_delete.is_enabled()

    def total_amount_sum(self):
        return self.find_element(loc.amount_sum)

    def found_search_field(self):
        return self.find_element(loc.search_field)

    def search_button_is_clickable(self):
        return self.find_element(loc.search_button)

    def change_name_button(self):
        return self.find_element(loc.change_button)

    def new_name_field(self):
        return self.find_element(loc.new_name_transaction)

    def confirm_name_button(self):
        return self.find_element(loc.name_confirm_button)

    def add_notes_button(self):
        return self.find_element(loc.add_note_button)

    def notes_field(self):
        return self.find_element(loc.note_field)

    def notes_confirm(self):
        return self.find_element(loc.note_confirm_button)

    def added_notes(self):
        return self.find_element(loc.added_notes_to_transaction)

    def add_or_edit_button(self):
        return self.find_element(loc.add_edit_button)

    def budget_fields(self):
        return self.find_element(loc.budget_field)

    def save_changes(self):
        return self.find_element(loc.save_changes_button)

    def new_budget(self):
        return self.find_element(loc.new_budget_sum)

    def status_checkboxes(self):
        return self.find_element(loc.status_confirm_checkbox)

    def change_status_checkboxes(self):
        return self.find_element(loc.changed_status)

    def account_is_swithed_to(self):
        return self.find_element(loc.account_info)

    def export_csv_button(self):
        return self.find_element(loc.export_csv_button)

    def count_selected_elements(self):
        return self.find_elements(loc.selected_elements)

    def find_changed_name_element(self):
        return self.find_element(loc.changed_name_element)

    def find_filter_transaction_elements(self):
        return self.find_elements(loc.filter_transaction_elements)
