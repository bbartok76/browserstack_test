from pytest import fixture
from pages.login_page import LoginPage
from modules.params import invalid_email_params


@fixture(scope="function")
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    page.wait_for_title()
    return page


@invalid_email_params
def test_login_with_invalid_email(login_page, email, password):
    login_page.login(email, password)
    login_page.sign_in.is_displayed()
    assert login_page.invalid_email_message.is_displayed()
    assert login_page.url == login_page.current_url
