from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """/html/body/div/main/div/div/div/form/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO_USER = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_POST = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE_NEW_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION_NEW_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_RES_LBl = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_FIND_CONTACT_US = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")

class OperationsHelper(BasePage, TestSearchLocators):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"we find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text
    def get_hello_text(self):
        hello_field = self.find_element(TestSearchLocators.LOCATOR_HELLO_USER, time=2)
        text = hello_field.text
        logging.info(f"we find text {text} in hello field {TestSearchLocators.LOCATOR_HELLO_USER[1]}")
        return text
    def click_create_new_post_btn(self):
        logging.info('click new post button')
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST).click()
    def enter_title_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_TITLE_NEW_POST[1]}")
        title_post = self.find_element(TestSearchLocators.LOCATOR_TITLE_NEW_POST)
        title_post.clear()
        title_post.send_keys(word)
    def enter_content_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_TITLE_NEW_POST[1]}")
        content_post = self.find_element(TestSearchLocators.LOCATOR_CONTENT_POST)
        content_post.clear()
        content_post.send_keys(word)
    def enter_description_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION_NEW_POST[1]}")
        description_post = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_NEW_POST)
        description_post.clear()
        description_post.send_keys(word)
    def click_save_btn(self):
        logging.info("click save post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()
    def click_contact_us_button(self):
        logging.info("Click Contact us button")
        self.find_element(TestSearchLocators.LOCATOR_FIND_CONTACT_US).click()

    def enter_your_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_YOUR_NAME[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME)
        login_field.clear()
        login_field.send_keys(word)
    def enter_your_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_YOUR_EMAIL[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL)
        email_field.clear()
        email_field.send_keys(word)
    def enter_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        content_field.clear()
        content_field.send_keys(word)
    def click_contact_us_end(self):
        logging.info("Click end button contact us")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()
    def get_res_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_RES_LBl, time=2)
        text = user_field.text
        logging.info(f"We find text {text} in res field {TestSearchLocators.LOCATOR_RES_LBl[1]}")
        return text
    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text