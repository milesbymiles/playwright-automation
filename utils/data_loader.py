"""Reads test data (request payloads) from the data/ folder."""
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_payload(name: str) -> dict:
    """load_payload("create_post") -> contents of data/payloads/create_post.json"""
    return json.loads((DATA_DIR / "payloads" / f"{name}.json").read_text())
