from selene.support.jquery_style_selectors import s

from src.pages.page import BasePage
from src.pages.users_page import UsersPage


class MainPage(BasePage):
    def __init__(self):
        self.loggedUser = s("#navbar > ul.nav.navbar-nav.navbar-right > li.user_info > span:nth-child(1) > strong")
        self.logo = s("a.navbar-brand")
        self.logout_btn = s("#logout")
        self.users_link = s("#users_link")

    def logout(self):
        self.logout_btn.click()

    def go_to_users_page(self):
        self.users_link.click()
        return UsersPage()
