from framework.locators.inventory_locators import InventoryLocators as L
from framework.pages.base_page import BasePage


class InventoryPage(BasePage):
    def get_title(self) -> str:
        return self.get_text(L.PAGE_TITLE)

    def add_product_to_cart(self, product_name: str):
        slug = product_name.lower().replace(" ", "-")
        self.click(L.add_to_cart_button(slug))

    def get_cart_count(self) -> str:
        return self.get_text(L.CART_BADGE)

    def open_cart(self):
        self.click(L.CART_LINK)

    def sort_products_by(self, option_text: str):
        self.select_option(L.SORT_DROPDOWN, option_text)

    def get_product_names(self) -> list[str]:
        self.wait_for_visible(L.PRODUCT_NAMES)  # all_inner_texts() does not auto-wait
        return self.get_all_texts(L.PRODUCT_NAMES)

    def get_product_prices(self) -> list[str]:
        self.wait_for_visible(L.PRODUCT_PRICES)
        return self.get_all_texts(L.PRODUCT_PRICES)
