# Python Playwright BDD Framework (UI + API)

Simple, interview-friendly framework using **Python, Playwright, pytest-bdd (Gherkin), Page Object Model,
Allure + HTML reports, GitHub Actions, and Playwright MCP**.

Practice sites: UI = https://www.saucedemo.com , API = https://jsonplaceholder.typicode.com

## Structure
```
features/            Gherkin .feature files (plain English test cases)
  ui/login.feature, ui/cart.feature, api/posts.feature
tests/
  test_*.py          one line each: binds a feature file to pytest
  steps/             step definitions (Gherkin sentence -> Python)
framework/
  locators/          selectors only (no logic)
  pages/             Page Objects: actions only (no assertions)
  api/               API client (Playwright APIRequestContext)
  config/settings.py URLs and credentials (env-overridable)
conftest.py          fixtures + failure-screenshot hook
.github/workflows/   CI pipeline
mcp/ + .mcp.json     Playwright MCP setup and guide
```
Flow: `feature file -> step definition -> page object -> locators -> browser`

## Setup
```bash
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run
```bash
pytest                    # everything
pytest -m smoke           # only @smoke scenarios
pytest -m ui              # only UI
pytest -m api             # only API
pytest --headed           # watch the browser
pytest --browser firefox  # other browser
```

## Reports
- HTML: `reports/report.html` (open in a browser)
- Allure: `allure serve reports/allure-results` (needs Allure CLI: https://allurereport.org/docs/install/)
- Failed UI tests: screenshot attached to Allure, Playwright trace in `reports/artifacts/`
  (view with `playwright show-trace <trace.zip>`)
