from urllib.parse import urljoin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from resources.locators import locators
from modules.context import ctx

SHORT_TIMEOUT = 3
LONG_TIMEOUT = 30


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.title = None
        self._name = "base_page"
        self._url = "/"

    @property
    def name(self) -> str:
        return self._name

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    @property
    def locators(self) -> dict:
        return {
            key: (loc["by"], loc["locator"]) for key, loc in locators.get(self.name, {}).items()
        }

    @property
    def url(self) -> str:
        return urljoin(ctx["base_url"], self._url)

    def open(self) -> None:
        self.driver.get(self.url)

    def wait_for_title(self) -> None:
        WebDriverWait(self.driver, LONG_TIMEOUT).until(EC.title_contains(self.title))

    def click(self, locator: tuple[str, str]) -> None:
        WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def enter_text(self, locator: tuple[str, str], text: str) -> None:
        WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)
