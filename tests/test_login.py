from selene.support.conditions import be
from selene.support.conditions import have
from selene import browser
from src.pages.login_page import LoginPage


def test_user_can_not_login_with_invalid_credentials(setup):
    (LoginPage()
     .open()
     .login_as("admin", "")
     .than()
     .password_err_label
     .should(have.exact_text("Field is required. Minimum 6 symbols length")))


def test_user_can_login_and_logout(setup):
    login = LoginPage()
    main_page = login.login_as("admin", "admin").than_at_main_page()
    main_page.loggedUser.should(have.exact_text("admin"))
    main_page.logout()
    login.username_input.should(be.visible)


# brutal fix for login =)

def teardown_module():
    browser.close()
