import pytest

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_add_a_product_to_the_cart(logged_in, inventory_page):
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    assert inventory_page.get_cart_count() == "1"


@pytest.mark.regression
def test_added_product_is_listed_in_the_cart(logged_in, inventory_page, cart_page):
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    assert "Sauce Labs Backpack" in cart_page.get_product_names()
