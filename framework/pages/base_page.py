from playwright.sync_api import Page


class BasePage:
    """Common actions every page object can reuse."""

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.locator(selector).click()

    def type_text(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def get_all_texts(self, selector: str) -> list[str]:
        return self.page.locator(selector).all_inner_texts()

    def wait_for_visible(self, selector: str):
        self.page.locator(selector).first.wait_for(state="visible")  # .first: selector may match many elements

    def select_option(self, selector: str, visible_text: str):
        # Works for a normal HTML <select> dropdown: pick an option by the text the user sees
        self.page.locator(selector).select_option(label=visible_text)
