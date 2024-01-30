from time import sleep
from pages.login_page import LoginPage
from modules.params import invalid_email_params


@invalid_email_params
def test_login_with_invalid_email(driver, email, password):
    page = LoginPage(driver)
    page.open()
    page.wait_for_title()
    page.login(email, password)
    page.sign_in.is_displayed()
    assert page.invalid_email.is_displayed()
    assert page.url == page.current_url
