import requests
from selenium.webdriver.support.select import Select
from src.pageFactory.utils.credentials import Credentials
from src.test.conftest import logger
from selenium.webdriver.common.by import By
from src.pageFactory.objectREpository.create_Account_page import CreateAccountPageObjects


class AccountCreate:
    def __init__(self, driver):
        self.driver = driver

    def account_type_selection(self):
        current_url = self.driver.current_url
        response = requests.get(current_url)
        status_code = response.status_code
        try:
            assert status_code == 200
            self.driver.find_element(By.XPATH, CreateAccountPageObjects.create_account_button).click()
            self.driver.find_element(By.XPATH, CreateAccountPageObjects.for_my_personal_use).click()
            logger.info("Navigating to next page")
        except Exception:
            logger.error("page load failed")
            raise Exception("page load failed")

    def entering_name(self):
        current_url = self.driver.current_url
        response = requests.get(current_url)
        status_code = response.status_code
        try:
            assert status_code == 200
            self.driver.find_element(By.XPATH, CreateAccountPageObjects.first_name_input).send_keys(Credentials.first_name)
            self.driver.find_element(By.XPATH, CreateAccountPageObjects.last_name_input).send_keys(Credentials.last_name)
            self.driver.find_element(By.XPATH, CreateAccountPageObjects.next_button).click()
            logger.info("Navigating to next page")
        except Exception:
            logger.error("page load failed")
            raise Exception("page load failed")

    def entering_dob_and_gender(self):
        current_url = self.driver.current_url
        response = requests.get(current_url)
        status_code = response.status_code
        try:
            assert status_code == 200
            month = Select(self.driver.find_element(By.XPATH, CreateAccountPageObjects.month_dropdown))
            month.select_by_value("5")
            self.driver.find_element(By.XPATH, CreateAccountPageObjects.day_input).send_keys(Credentials.day)
            self.driver.find_element(By.XPATH, CreateAccountPageObjects.year_input).send_keys(Credentials.year)
            gender = Select(self.driver.find_element(By.XPATH, CreateAccountPageObjects.gender_dropdown))
            gender.select_by_value("1")
            self.driver.find_element(By.XPATH, CreateAccountPageObjects.next_button).click()
            logger.info("Navigating to next page")
        except Exception:
            logger.error("page load failed")
            raise Exception("page load failed")