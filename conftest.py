import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from modules.context import ctx


def pytest_addoption(parser):
    parser.addoption(
        "--base-page",
        action="store",
        default="https://www.browserstack.com",
        help="The root url of the tested site",
    )


@pytest.fixture(scope="session", autouse=True)
def init(request):
    ctx["base_url"] = request.config.getoption("--base-page")


@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--allow-running-insecure-content')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    with webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    ) as _driver:
        yield _driver
