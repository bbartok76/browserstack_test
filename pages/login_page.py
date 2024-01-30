from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage, SHORT_TIMEOUT


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.title = "BrowserStack Login"
        self._name = "login_page"
        self._url = "/users/sign_in"

    @property
    def email(self):
        return WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located(self.locators["email"])
        )

    @property
    def password(self):
        return WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located(self.locators["password"])
        )

    @property
    def sign_in(self):
        return WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located(self.locators["sign_in"])
        )

    @property
    def invalid_email(self):
        return WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located(self.locators["invalid_email"])
        )

    def login(self, email, password) -> None:
        self.enter_text(self.locators["email"], email)
        self.enter_text(self.locators["password"], password)
        self.click(self.locators["sign_in"])
