from playwright.sync_api import sync_playwright, Page,expect
import pytest

def alert(page:Page):
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")
        page.on ("dialog", lambda dialog: dialog.accept())
        page.get_by_role("button", name="Click for JS Alert").click()

@pytest.mark.regression
def test_alert():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=150)
            context = browser.new_context()
            page = context.new_page()
            try:
                alert(page)       
                expect(page.locator("#result")).to_have_text("You successfully clicked an alert")
                print(f"\nAlert test passed")
            except Exception as e:
                print(e)
            browser.close()