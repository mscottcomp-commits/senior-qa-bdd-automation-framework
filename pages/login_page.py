class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.products_title = page.locator(".title")
        self.error_message = page.locator("[data-test='error']")

    def open_login_page(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def is_products_page_visible(self):
        return self.products_title.inner_text() == "Products"

    def is_error_message_visible(self):
        return self.error_message.is_visible()