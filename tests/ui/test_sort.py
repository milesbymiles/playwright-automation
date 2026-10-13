import pytest

pytestmark = pytest.mark.ui


@pytest.mark.parametrize("option, first_product", [
    pytest.param("Name (Z to A)", "Test.allTheThings() T-Shirt (Red)", marks=pytest.mark.regression),
    pytest.param("Price (low to high)", "Sauce Labs Onesie", marks=pytest.mark.smoke),
])
def test_sort_products(logged_in, inventory_page, option, first_product):
    inventory_page.sort_products_by(option)

    assert inventory_page.get_product_names()[0] == first_product
