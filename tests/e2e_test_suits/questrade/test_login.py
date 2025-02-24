import pytest
from locators.questrade.login import QuestradeAuthLocators  # Import locators

@pytest.mark.smoke
def test_questrade_login(questrade_login_fixture):
    page = questrade_login_fixture  # This is the logged-in page
    locators = QuestradeAuthLocators(page)  # Instantiate locator class

    # ✅ Check if login was successful by verifying the page title
    assert page.title() == "Secure Page page for Automation Testing Practice"
    page.screenshot(path="questrade_login.png")

    # ✅ Check if the page URL is correct
    assert page.url == "https://practice.expandtesting.com/secure"

    # ✅ Check if logout button is visible (means login was successful)
    assert locators.logout.profile_logout_button.is_visible()
