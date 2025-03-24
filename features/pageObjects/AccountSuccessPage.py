from selenium.webdriver.common.by import By


class AccountSuccessPage:
    def __init__(self,driver):
        self.driver = driver

    your_account_has_been_created_xpath = "//div[@id='content']/h1"

    def display_status_of_account_successfully_created(self,expected_text):
        return self.driver.find_element(By.XPATH, self.your_account_has_been_created_xpath).text.__eq__(expected_text)