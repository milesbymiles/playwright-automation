# Python Playwright Framework (UI + API)

Simple, interview-friendly framework using **Python, pytest + pytest-playwright, Page Object Model,
HTML report + Playwright trace viewer, GitHub Actions, and Playwright MCP**.

Practice sites: UI = https://www.saucedemo.com , API = https://jsonplaceholder.typicode.com

## Structure
```
tests/
  ui/                test_login.py, test_cart.py, test_sort.py, test_products_excel.py
  api/               test_posts.py (uses the `api` fixture from conftest)
pages/               Page Objects: actions only (no assertions)
locators/            selectors only (no logic)
config/              settings.py (URLs, environments) + secrets.py (Vault -> env var)
utils/               data_loader.py (JSON), excel_util.py (Excel)
data/                payloads/ (JSON) and test_data/ (Excel)
conftest.py          fixtures (page objects, api, logged_in) + --all-browsers
pytest.ini           markers and report/trace options
.github/workflows/   CI pipeline
mcp/ + .mcp.json     Playwright MCP setup and guide
```
Flow: `test -> page object -> locators -> browser`  (assertions live in the test)

## Setup
```bash
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run
```bash
pytest                    # everything
pytest -m smoke           # only smoke tests
pytest -m ui              # only UI
pytest -m api             # only API
pytest --headed           # watch the browser
pytest --browser firefox  # other browser
pytest --all-browsers     # chromium + firefox + webkit
```

## Reports
- HTML: `reports/report.html` (open in a browser)
- Failed UI tests: screenshot and Playwright trace saved in `reports/artifacts/`
  (view with `playwright show-trace <trace.zip>`)
