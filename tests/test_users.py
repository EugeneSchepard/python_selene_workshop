from selene.support.conditions import have

from src.domain.user import User
from src.pages.login_page import LoginPage


def test_can_add_new_user(setup):
    user = User("dodo", "123456", "dodo@mail.com")
    (LoginPage()
     .open()
     .login_as("admin", "admin")
     .than_at_main_page()
     .go_to_users_page()
     .add_new_user(user)
     .table
     .user_names()
     .should(have.texts("admin", "dodo")))
