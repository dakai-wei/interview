from playwright.sync_api import Page

class BaseLocators: # Base Class for all locators
        def __init__(self, page: Page):
                self.page = page
                self.profile = page.get_by_role("button", name="Profile")
        

class QuestradeLoginLocators(BaseLocators): # Inherit from BaseLocators
        def __init__(self, page: Page):
                super().__init__(page)
                self.username = page.locator("#username")
                self.password = page.locator("#password")
                self.sign_in_button = page.get_by_role("button", name="Login")

class QuestradeLogoutLocators(BaseLocators):
        def __init__(self, page: Page):
                super().__init__(page)
                self.profile_logout_button = page.get_by_role("link", name="Logout")
        
        
class QuestradeAuthLocators: 
        def __init__(self, page: Page):
                self.login = QuestradeLoginLocators(page)
                self.logout = QuestradeLogoutLocators(page)
        # Wrapper Class, combine both classes into one wrapper class, making it easier to access everything