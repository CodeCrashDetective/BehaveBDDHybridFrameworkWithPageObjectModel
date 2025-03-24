from behave import *
from features.pageObjects.HomePage import HomePage
from features.pageObjects.SearchPage import SearchPage


@given(u'I got navigated to Home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.check_home_page_title("Your Store")


@when(u'I enter valid product say "{product}" into the Search box field')
def step_impl(context, product):
    context.home_page.enter_product_into_search_box_field(product)


@when(u'I click on Search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    assert context.search_page.display_status_of_product()


@when(u'I enter invalid product say "{product}" into the Search box field')
def step_impl(context, product):
    context.home_page.enter_product_into_search_box_field(product)


@then(u'Proper massage should be displayed in Search results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.search_page.display_status_of_massage(expected_text)


@when(u'I dont enter anything into Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("")






