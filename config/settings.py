"""One place for all configuration. Override with environment variables in CI."""
import os

from config.secrets import get_secret

# Pick the environment with TEST_ENV=int|stg|prod (default: int)
# NOTE: the practice sites have only one environment, so all three point to the same URLs.
# On a real project each environment gets its own URLs here.
ENVIRONMENTS = {
    "int":  {"ui": "https://www.saucedemo.com", "api": "https://jsonplaceholder.typicode.com"},
    "stg":  {"ui": "https://www.saucedemo.com", "api": "https://jsonplaceholder.typicode.com"},
    "prod": {"ui": "https://www.saucedemo.com", "api": "https://jsonplaceholder.typicode.com"},
}
TEST_ENV = os.getenv("TEST_ENV", "int")

UI_BASE_URL = os.getenv("UI_BASE_URL", ENVIRONMENTS[TEST_ENV]["ui"])
API_BASE_URL = os.getenv("API_BASE_URL", ENVIRONMENTS[TEST_ENV]["api"])

# Password comes from Vault (key "password" at secret/saucedemo), else env var, else public demo default
PASSWORD = get_secret("password", "UI_PASSWORD", default="secret_sauce")
