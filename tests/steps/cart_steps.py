from pytest_bdd import when, then, parsers


@when(parsers.parse('the user adds "{product}" to the cart'))
def add_product(inventory_page, product):
    inventory_page.add_product_to_cart(product)


@when("the user opens the cart")
def open_cart(inventory_page):
    inventory_page.open_cart()


@then(parsers.parse('the cart badge shows "{count}"'))
def cart_badge_shows(inventory_page, count):
    assert inventory_page.get_cart_count() == count


@then(parsers.parse('the cart page lists "{product}"'))
def cart_lists_product(cart_page, product):
    assert product in cart_page.get_product_names()
