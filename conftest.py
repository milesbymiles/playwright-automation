import pytest

from config.settings import API_BASE_URL, PASSWORD
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


# ---------- Run every test on all browsers: pytest --all-browsers ----------
ALL_BROWSERS = ["chromium", "firefox", "webkit"]  # webkit = Safari engine


def pytest_addoption(parser):
    parser.addoption("--all-browsers", action="store_true", help="Run every test on chromium, firefox and webkit")


def pytest_configure(config):
    # pytest-playwright runs each test once per name in the --browser list
    if config.getoption("--all-browsers"):
        config.option.browser = ALL_BROWSERS


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


@pytest.fixture
def logged_in(page):
    """Open the site and log in as standard_user."""
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login("standard_user", PASSWORD)


# ---------- API fixture: Playwright's request object, base URL already set ----------
@pytest.fixture
def api(playwright):
    request_context = playwright.request.new_context(base_url=API_BASE_URL)
    yield request_context
    request_context.dispose()
