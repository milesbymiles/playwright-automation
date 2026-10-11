class InventoryLocators:
    PAGE_TITLE = ".title"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    @staticmethod
    def add_to_cart_button(product_slug: str) -> str:
        # "Sauce Labs Backpack" -> add-to-cart-sauce-labs-backpack
        return f"[data-test='add-to-cart-{product_slug}']"

    SORT_DROPDOWN = "[data-test='product-sort-container']"
    PRODUCT_NAMES = ".inventory_item_name"
