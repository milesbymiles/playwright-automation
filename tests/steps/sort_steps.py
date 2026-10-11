from pytest_bdd import when, then, parsers


@when(parsers.parse('the user sorts products by "{option}"'))
def sort_products(inventory_page, option):
    inventory_page.sort_products_by(option)


@then(parsers.parse('the first product is "{product}"'))
def first_product_is(inventory_page, product):
    names = inventory_page.get_product_names()
    assert names[0] == product
