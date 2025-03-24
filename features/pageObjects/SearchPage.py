from selenium.webdriver.common.by import By
from features.pageObjects.BasePage import BasePage
class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    valid_product_link_text = "HP LP3065"
    warning_massage_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_product(self):
        return self.display_status("valid_product_link_text",self.valid_product_link_text)

    def display_status_of_massage(self,expected_massage_text):
        return self.retrieved_element_text_equals("warning_massage_xpath", self.warning_massage_xpath, expected_massage_text)


