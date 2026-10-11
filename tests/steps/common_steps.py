"""Steps shared by more than one feature file."""
from pytest_bdd import given, parsers

from framework.config.settings import PASSWORD


@given("the user is on the login page")
def open_login_page(login_page):
    login_page.open_login_page()


@given(parsers.parse('the user is logged in as "{username}"'))
def logged_in_user(login_page, username):
    login_page.open_login_page()
    login_page.login(username, PASSWORD)
