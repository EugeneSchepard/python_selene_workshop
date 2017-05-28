from selene.support.jquery_style_selectors import s

from src.pages.page import BasePage


class UsersPage(BasePage):
    def __init__(self):
        self.user_name_input = s("#inputNewUserName")
        self.user_password_input = s("#inputNewUserPassword")
        self.user_email_input = s("#newUserEmail")
        self.add_btn = s("#add_new_user_btn")

    def add_new_user(self, user):
        self.user_email_input.set(user.name)
        self.user_password_input.set(user.password)
        self.user_email_input.set(user.email)
        self.add_btn.click()
