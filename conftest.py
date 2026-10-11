import pytest

from framework.api.api_client import ApiClient
from framework.config.settings import API_BASE_URL
from framework.pages.cart_page import CartPage
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage

# Register the step files so every feature can use them
pytest_plugins = [
    "tests.steps.common_steps",
    "tests.steps.login_steps",
    "tests.steps.cart_steps",
    "tests.steps.sort_steps",
    "tests.steps.excel_steps",
    "tests.steps.api_steps",
]


# ---------- Run every test on all browsers (parametrization) ----------
ALL_BROWSERS = ["chromium", "firefox", "webkit"]  # webkit = Safari engine


def pytest_addoption(parser):
    parser.addoption("--all-browsers", action="store_true", help="Run every test on chromium, firefox and webkit")


def pytest_configure(config):
    # pytest-playwright creates one test per name in the --browser list (it parametrizes `browser_name`).
    # So filling that list is all we need to run each test 3 times.
    if config.getoption("--all-browsers"):
        config.option.browser = ALL_BROWSERS


@pytest.hookimpl(tryfirst=True)
def pytest_generate_tests(metafunc):
    # pytest-playwright only parametrizes tests that list `page` in their arguments.
    # BDD tests get `page` indirectly (through the step fixtures), so we add `browser_name`
    # ourselves for every @ui test. The plugin then creates one test per browser.
    if metafunc.definition.get_closest_marker("ui") and "browser_name" not in metafunc.fixturenames:
        metafunc.fixturenames.append("browser_name")


# ---------- Page object fixtures (the "page" fixture comes from pytest-playwright) ----------
@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


# ---------- API fixture ----------
@pytest.fixture
def api_client(playwright):
    request_context = playwright.request.new_context(base_url=API_BASE_URL)
    yield ApiClient(request_context)
    request_context.dispose()
