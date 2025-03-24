from selenium.webdriver.common.by import By
from features.pageObjects.AccountSuccessPage import AccountSuccessPage
from features.pageObjects.BasePage import BasePage

class RegisterPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    privacy_policy_checkbox_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    newsletter_button_xpath = "//input[@name='newsletter' and @value='1']"
    duplicate_email_warning_massage = "//div[@class='alert alert-danger alert-dismissible']"
    privacy_policy_warning_massage_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_massage_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_massage_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_massage_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_massage_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_massage_xpath = "//input[@id='input-password']/following-sibling::div"


    def enter_first_name_into_the_field(self,first_name_text):
        self.type_into_element("first_name_field_id", self.first_name_field_id, first_name_text)


    def enter_last_name_into_the_field(self,last_name_text):
        self.type_into_element("last_name_field_id", self.last_name_field_id, last_name_text)


    def enter_email_address_into_the_field(self,email_text):
        self.type_into_element("email_field_id", self.email_field_id, email_text)


    def enter_telephone_into_the_field(self,telephone_no):
        self.type_into_element("telephone_field_id", self.telephone_field_id, telephone_no)


    def enter_password_into_the_field(self,password_text):
        self.type_into_element("password_field_id", self.password_field_id, password_text)


    def enter_confirm_password_into_the_field(self,confirm_password_text):
        self.type_into_element("confirm_password_field_id", self.confirm_password_field_id, confirm_password_text)


    def select_privacy_policy_option(self):
        self.click_on_element("privacy_policy_checkbox_name", self.privacy_policy_checkbox_name)


    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def select_newsletter_option(self):
        self.click_on_element("newsletter_button_xpath", self.newsletter_button_xpath)


    def display_status_of_duplicate_mail_warning(self,expected_text):
        return self.retrieved_element_text_contains("duplicate_email_warning_massage", self.duplicate_email_warning_massage, expected_text)


    def display_status_of_all_warning_massages(self,expected_privacy_policy_warning,expected_first_name_warning,expected_last_name_warning,expected_email_warning,expected_telephone_warning,expected_password_warning):
        privacy_status = self.retrieved_element_text_contains("privacy_policy_warning_massage_xpath",
                                             self.privacy_policy_warning_massage_xpath,
                                             expected_privacy_policy_warning)
        first_name_status = self.retrieved_element_text_equals("self.first_name_warning_massage_xpath",
                                                               self.first_name_warning_massage_xpath,
                                                               expected_first_name_warning)
        last_name_status = self.retrieved_element_text_equals("last_name_warning_massage_xpath",
                                                    self.last_name_warning_massage_xpath,
                                                    expected_last_name_warning)
        email_status = self.retrieved_element_text_equals("email_warning_massage_xpath",
                                                self.email_warning_massage_xpath,
                                                expected_email_warning)
        telephone_status = self.retrieved_element_text_equals("telephone_warning_massage_xpath",
                                                              self.telephone_warning_massage_xpath,
                                                              expected_telephone_warning)
        password_status = self.retrieved_element_text_equals("password_warning_massage_xpath",
                                                             self.password_warning_massage_xpath,
                                                             expected_password_warning)
        return self.return_find_status(privacy_status, first_name_status, last_name_status, email_status, telephone_status, password_status)

