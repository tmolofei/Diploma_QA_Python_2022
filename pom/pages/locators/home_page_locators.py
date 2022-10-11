from datetime import date
from selenium.webdriver.common.by import By


addtransaction_button = (By.XPATH, '//a[@class="btn addTransaction"]')
add_expenses_button = (By.XPATH, '//*[@id="wrapper-accounts"]/ul/li/div/div[2]/a[1]')
logout_button = (By.XPATH, '//*[@id="unav"]/li[2]/a')
accounts_button = (By.XPATH, '//*[@id="wrapper-envelopes-accounts"]/ul/li[2]/a')
account_info = (By.XPATH, '//*[@id="wrapper-accounts"]/ul/li/ul/li/ul/li/div/div[1]/p/strong')
envelopes_button = (By.XPATH, '//*[@id="wrapper-envelopes-accounts"]/ul/li[1]/a')
goodbye_text = (
    By.XPATH, '//*[@id="content"]/div/div/div/section[1]/div/div/div/div/div/div[2]/div/h3'
)

date_field = (By.ID, 'expense-date')
current_date = date.today().strftime('%d/%m/%Y')
payee_field = (By.ID, 'expense-receiver')
amount_field = (By.ID, 'expense-amount')
envelope_field = (By.XPATH, '//*[@id="expenseCredit"]/form/fieldset/div[4]/div/select')
save_button = (By.ID, 'addTransactionSave')
added_new_payee_1 = (By.XPATH, '//*[@id="transactions-tbody"]/tr[2]/td[2]')
payee_checkbox = (By.XPATH, '//i[@class="icon-type-debit"]')
transactions_count = (By.XPATH, '//tr[@class="selected"]')
delete_button = (By.ID, 'bulk-edit-delete-link')
all_checkbox_button = (By.XPATH, '//span[@class="header"]')
amount_sum = (By.XPATH, '//*[@id="wrapper-envelopes"]/ul/li/div/div[1]/div/ul/li/div[2]/strong')
search_field = (By.CSS_SELECTOR, 'input[placeholder="Search"]')
search_button = (By.ID, 'trans-search-btn')
change_button = (By.ID, 'bulk-edit-name-link')
new_name_transaction = (By.XPATH, '/html/body/div[6]/div[2]/form/fieldset/div/div/input')
name_confirm_button = (By.XPATH, '//*[@id="bulkEditNameSave"]')
add_note_button = (By.ID, 'bulk-edit-add-note-link')
note_field = (By.XPATH, '//*[@id="bulk-notes"]')
note_confirm_button = (By.XPATH, '//*[@id="bulkEditAddNoteSave"]')
added_notes_to_transaction = (By.XPATH, '//*[@id="transactions-tbody"]/tr[2]/th[2]/a')
add_edit_button = (By.XPATH, '//*[@id="wrapper-envelopes"]/ul/li/div/div[2]/a[1]')
budget_field = (
    By.XPATH, '//*[@id="4"]/envelope-row/row-template/fieldset/div[3]/div/div[2]/div/input'
)
save_changes_button = (By.ID, 'save-envelopes-btn')
new_budget_sum = (By.XPATH, '//*[@id="wrapper-envelopes"]/ul/li/ul/li[2]/ul/li[4]/div/div[2]/p/em')
status_confirm_checkbox = (By.XPATH, '//i[@class="icon-status-ck-wh-sm"]')
changed_status = (By.XPATH, '//i[@class="icon-status-ck-grn-sm"]')
export_csv_button = (By.ID, 'export-txns')
selected_elements = (By.XPATH, '//tr[@class="selected"]')
changed_name_element = (By.XPATH, '//*[@id="transactions-tbody"]/tr[2]/th[2]')
filter_transaction_elements = (By.XPATH, '//*[@id="transactions-tbody"]/tr[2]/th[2]')
