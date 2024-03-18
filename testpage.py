from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_NAME_FIELD = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_EMAIL_FIELD = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTENT_TEXTAREA = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACT_BUTTON = (By.XPATH, '//*[@id="contact"]/div[4]/button')


class OperationsHelper(BasePage):
    def enter_name(self, word):
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email(self, word):
        email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    def enter_content(self, word):
        textarea = self.find_element(TestSearchLocators.LOCATOR_CONTENT_TEXTAREA)
        textarea.clear()
        textarea.send_keys(word)

    def submit_contact(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BUTTON).click()

    def get_alert_text(self):
        alert = self.driver.switch_to_alert
        return alert.text
