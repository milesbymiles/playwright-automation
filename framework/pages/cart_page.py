from framework.locators.cart_locators import CartLocators as L
from framework.pages.base_page import BasePage


class CartPage(BasePage):
    def get_title(self) -> str:
        return self.get_text(L.PAGE_TITLE)

    def get_product_names(self) -> list[str]:
        # all_inner_texts() does not auto-wait, so wait for the cart list first
        self.wait_for_visible(L.CART_LIST)
        return self.get_all_texts(L.CART_ITEM_NAMES)
