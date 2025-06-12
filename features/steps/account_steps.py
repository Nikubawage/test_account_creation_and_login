from behave import given, when, then
from utils.driver_factory import get_driver
from pages.home_page import HomePage
from pages.create_account_page import CreateAccountPage
from pages.login_page import LoginPage
import time
import os

# Test data
timestamp = int(time.time())
email = f"nikita.bawage{timestamp}@testmail.com"
first_name = "Nikita"
last_name = "Bawage"
password = "Test@1234"

# Ensure screenshots folder exists
os.makedirs("screenshots", exist_ok=True)

@given('the user launches the browser')
def step_impl(context):
    context.driver = get_driver()

@when('the user navigates to the home page')
def step_impl(context):
    context.driver.get("https://magento.softwaretestingboard.com/")
    context.home_page = HomePage(context.driver)

@when('the user creates a new account')
def step_impl(context):
    context.home_page.go_to_create_account()
    create_page = CreateAccountPage(context.driver)
    create_page.enter_first_name(first_name)
    create_page.enter_last_name(last_name)
    create_page.enter_email(email)
    create_page.enter_password(password)
    create_page.enter_confirm_password(password)
    create_page.click_create_account()

    # 📸 Screenshot after account creation
    context.driver.save_screenshot(f"screenshots/after_account_creation_{timestamp}.png")

@when('the user logs out')
def step_impl(context):
    context.home_page.logout()

@when('the user logs in with the same account')
def step_impl(context):
    context.home_page.go_to_login()
    login_page = LoginPage(context.driver)
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login()

@then('the user should see the welcome message')
def step_impl(context):
    assert context.home_page.is_user_logged_in()

    # 📸 Screenshot after login
    context.driver.save_screenshot(f"screenshots/after_login_{timestamp}.png")

@then('the browser is closed')
def step_impl(context):
    context.driver.quit()