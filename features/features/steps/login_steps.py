from behave import given, when, then
from pages.login_page import LoginPage


@given("I am on the SauceDemo login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open_login_page()


@when("I login with valid credentials")
def step_login_valid_user(context):
    context.login_page.login("bad_user", "bad_password")

@then("I should see the products page")
def step_verify_products_page(context):
    assert False


@when("I login with invalid credentials")
def step_login_invalid_user(context):
    context.login_page.login("bad_user", "bad_password")


@then("I should see a login error message")
def step_verify_login_error(context):
    assert context.login_page.is_error_message_visible()