import pytest

from config.settings import PASSWORD

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_login_with_valid_credentials(login_page, inventory_page):
    login_page.open_login_page()
    login_page.login("standard_user", PASSWORD)

    assert inventory_page.get_title() == "Products"


@pytest.mark.regression
@pytest.mark.parametrize("username, password, message", [
    ("locked_out_user", PASSWORD, "locked out"),
    ("standard_user", "wrong_pass", "do not match any user"),
])
def test_login_fails_with_invalid_details(login_page, username, password, message):
    login_page.open_login_page()
    login_page.login(username, password)

    assert message in login_page.get_error_message()
