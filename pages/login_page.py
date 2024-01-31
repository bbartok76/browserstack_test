from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage, SHORT_TIMEOUT


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.title = "BrowserStack Login"
        self._name = "login_page"
        self._url = "/users/sign_in"

    @property
    def email(self) -> WebElement:
        return WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located(self.locators["email"])
        )

    @property
    def password(self) -> WebElement:
        return WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located(self.locators["password"])
        )

    @property
    def sign_in(self) -> WebElement:
        return WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located(self.locators["sign_in"])
        )

    @property
    def invalid_email_message(self) -> WebElement:
        return WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located(self.locators["invalid_email"])
        )

    def login(self, email, password) -> None:
        self.enter_text(self.locators["email"], email)
        self.enter_text(self.locators["password"], password)
        self.click(self.locators["sign_in"])
