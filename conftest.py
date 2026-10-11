import allure
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
    "tests.steps.api_steps",
]


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


# ---------- Attach a screenshot to the Allure report when a UI test fails ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
