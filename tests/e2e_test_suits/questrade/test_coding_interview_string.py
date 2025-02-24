import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.fixture
def example():
    p = sync_playwright().start()
    browser = p.chromium.launch()
    page = browser.new_page()
    yield page  # Yield only the `Page` object
    browser.close()
    p.stop()

def work_flow(page: Page):  # Pass `page` as an argument
    page.goto("https://practice.expandtesting.com/")
    page.screenshot(path="example1.png")
    expect(page).to_have_title('Practice Test Automation WebSite')

def test_example(example):  # This is needed to run with pytest
    work_flow(example)  # Pass `example` (which is a `Page` instance) to `work_flow`