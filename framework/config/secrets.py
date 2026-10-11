"""Reads secrets (like the password). Order of lookup:
1. HashiCorp Vault  - if VAULT_ADDR and VAULT_TOKEN are set
2. Environment variable
3. Default value (only OK for public demo data)
"""
import os


def _read_from_vault(path: str, key: str):
    address, token = os.getenv("VAULT_ADDR"), os.getenv("VAULT_TOKEN")
    if not (address and token):
        return None  # Vault not configured, skip it

    import hvac  # imported here so the framework runs even without hvac installed

    client = hvac.Client(url=address, token=token)
    secret = client.secrets.kv.v2.read_secret_version(path=path, raise_on_deleted_version=True)
    return secret["data"]["data"][key]


def get_secret(key: str, env_name: str, default: str = None, vault_path: str = "saucedemo"):
    return _read_from_vault(vault_path, key) or os.getenv(env_name, default)
