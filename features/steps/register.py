from behave import *
from features.pageObjects.AccountSuccessPage import AccountSuccessPage
from features.pageObjects.HomePage import HomePage
from features.pageObjects.RegisterPage import RegisterPage
from utilities import EmailWithTimesStampGenerator


@given(u'I navigate to Register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.select_register_option()


@when(u'I enter below details into mandatory fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name_into_the_field(row["firstname"])
        context.register_page.enter_last_name_into_the_field(row["lastname"])
        new_email = EmailWithTimesStampGenerator.get_new_email_with_timestamp()
        context.register_page.enter_email_address_into_the_field(new_email)
        context.register_page.enter_telephone_into_the_field(row["telephone"])
        context.register_page.enter_password_into_the_field(row["password"])
        context.register_page.enter_confirm_password_into_the_field(row["password"])


@when(u'I select Privacy policy option')
def step_impl(context):
    context.register_page.select_privacy_policy_option()


@when(u'I click on Continue button')
def step_impl(context):
    context.account_success_page = context.register_page.click_on_continue_button()


@then(u'Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    assert context.account_success_page.display_status_of_account_successfully_created(expected_text)


@when(u'I enter below details into all fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name_into_the_field(row["firstname"])
        context.register_page.enter_last_name_into_the_field(row["lastname"])
        new_email = EmailWithTimesStampGenerator.get_new_email_with_timestamp()
        context.register_page.enter_email_address_into_the_field(new_email)
        context.register_page.enter_telephone_into_the_field(row["telephone"])
        context.register_page.enter_password_into_the_field(row["password"])
        context.register_page.enter_confirm_password_into_the_field(row["password"])
        context.register_page.select_newsletter_option()


@when(u'I enter details into all fields except email')
def step_impl(context):
    context.register_page.enter_first_name_into_the_field("Asif")
    context.register_page.enter_last_name_into_the_field("Shaikh")
    context.register_page.enter_telephone_into_the_field("1234567890")
    context.register_page.enter_password_into_the_field("12345")
    context.register_page.enter_confirm_password_into_the_field("12345")
    context.register_page.select_newsletter_option()


@when(u'I enter existing email into email field')
def step_impl(context):
    context.register_page.enter_email_address_into_the_field("assifgshaikh@gmail.com")


@then(u'Proper warning massage informing about duplicate account should be displayed')
def step_impl(context):
    expected_warning = "Warning: E-Mail Address is already registered!"
    assert context.register_page.display_status_of_duplicate_mail_warning(expected_warning)


@when(u'I dont enter any details into the fields')
def step_impl(context):
    context.register_page.enter_first_name_into_the_field("")
    context.register_page.enter_last_name_into_the_field("")
    context.register_page.enter_telephone_into_the_field("")
    context.register_page.enter_password_into_the_field("")
    context.register_page.enter_confirm_password_into_the_field("")


@then(u'Proper warning massage for every mandatory fields should be displayed')
def step_impl(context):
    expected_privacy_policy_warning_massage = "Warning: You must agree to the Privacy Policy!"
    expected_first_name_warning_massage = "First Name must be between 1 and 32 characters!"
    expected_last_name_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"

    assert context.register_page.display_status_of_all_warning_massages(expected_privacy_policy_warning_massage
                                                                          ,expected_first_name_warning_massage
                                                                          ,expected_last_name_warning
                                                                          ,expected_email_warning
                                                                          ,expected_telephone_warning
                                                                          ,expected_password_warning)









