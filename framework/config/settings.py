"""One place for all configuration. Override with environment variables in CI."""
import os

from framework.config.secrets import get_secret

UI_BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")
API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")

# Password comes from Vault (key "password" at secret/saucedemo), else env var, else public demo default
PASSWORD = get_secret("password", "UI_PASSWORD", default="secret_sauce")
