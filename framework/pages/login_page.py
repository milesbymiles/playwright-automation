from framework.config.settings import UI_BASE_URL
from framework.locators.login_locators import LoginLocators as L
from framework.pages.base_page import BasePage


class LoginPage(BasePage):
    def open_login_page(self):
        self.open(UI_BASE_URL)

    def login(self, username: str, password: str):
        self.type_text(L.USERNAME_INPUT, username)
        self.type_text(L.PASSWORD_INPUT, password)
        self.click(L.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(L.ERROR_MESSAGE)
