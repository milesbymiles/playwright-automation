from pytest_bdd import when, then, parsers

from framework.config.settings import PASSWORD


@when(parsers.parse('the user logs in with username "{username}" and the correct password'))
def login_with_correct_password(login_page, username):
    login_page.login(username, PASSWORD)


@when(parsers.parse('the user logs in with username "{username}" and password "{password}"'))
def login_with_password(login_page, username, password):
    login_page.login(username, password)


@then("the Products page is shown")
def products_page_shown(inventory_page):
    assert inventory_page.get_title() == "Products"


@then(parsers.parse('the error message contains "{expected}"'))
def error_message_contains(login_page, expected):
    assert expected in login_page.get_error_message()
