from selene import browser
from selene.support.jquery_style_selectors import s

from src.pages.main_page import MainPage
from src.pages.page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        self.username_input = s("#inputEmail3")
        self.password_input = s("#inputPassword3")
        self.login_btn = s("#parent > form > div:nth-child(3) > div > button")
        self.password_err_label = s("#parent > form > div:nth-child(2) > div > div > ul > li")

    def open(self, url="/"):
        browser.open_url(url)
        return self

    def login_as(self, user, password):
        self.username_input.set(user)
        self.password_input.set(password)
        self.login_btn.click()
        return self

    def than(self):
        return self

    def than_at_main_page(self):
        return MainPage()
