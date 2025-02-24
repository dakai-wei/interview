class pcpartpicker_auth:

    login_banner_button = page.get_by_role("banner").get_by_role("link", name="Log In")
    username = page.get_by_role("textbox", name="Username or Email")
    password = page.get_by_role("textbox", name="Password")
    sign_in_button = page.get_by_role("button", name="Sign In")
    

    logout_banner_button = page.get_by_role("banner").get_by_role("link", name="Log Out")
    logout_button = page.get_by_role("button", name="Log Out")