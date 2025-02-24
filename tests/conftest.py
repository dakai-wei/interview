import pytest, allure
from playwright.sync_api import Playwright, sync_playwright, Page, expect
from utils.config import *
from locators.questrade.login import QuestradeAuthLocators


@pytest.fixture(scope="function")
def open_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page  # Provide the page instance to the test
        context.close()
        browser.close()
        
@pytest.fixture
def questrade_login_fixture(open_browser):
    page = open_browser
    locators = QuestradeAuthLocators(page)
    

    try:
        page.goto(questrade_URL)
        with allure.step("Enter username and password"):
            locators.login.username.fill(questrade_CREDENTIALS["username"])
            locators.login.password.fill(questrade_CREDENTIALS["password"])
        with allure.step("Click on sign in button"):
            locators.login.sign_in_button.click()
        yield page  # Return the logged-in page for the test to use
        with allure.step("Click on logout button"):
            locators.logout.profile_logout_button.click()
    finally:
        page.close() # In Python, finally ensures that cleanup actions always run, even if an error occurs.