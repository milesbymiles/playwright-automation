# How to explain this framework in an interview

## 30-second pitch
"It's a Python Playwright framework on pytest, using the Page Object Model. Tests are plain pytest functions with
the assertions inside them. Page objects hold the actions and a separate locators layer holds the selectors.
It covers UI and API with the same tool, gives an HTML report with screenshots and traces on failure, runs
tests on Chromium, Firefox and WebKit, and runs in GitHub Actions on every push."

## The layers (draw this on the whiteboard)
```
Test file         tests/ui/*.py, tests/api/*.py   - the scenario + assertions
      |
Page Object       pages/*.py                      - user actions (no assertions)
      |
Locators          locators/*.py                   - selectors only
      |
Playwright -> browser / API

Support: conftest.py (fixtures) | config/ (URLs, Vault) | data/ + utils/ (JSON, Excel) | CI
```
Rule of thumb: **tests = what + verify, pages = how, locators = where**.

## Design decisions and why
| Decision | Reason |
|---|---|
| Separate locators file | A UI change = a one-line fix in one place |
| No assertions in page objects | Pages stay reusable; the test decides pass/fail |
| Playwright for API too | One tool, one report, no extra library |
| Fixtures in conftest | Browser/API setup, page objects and login are automatic |
| Markers (smoke, regression, ui, api) | Run subsets: `pytest -m smoke` first in CI |
| `@pytest.mark.parametrize` | Same test, many data rows (login failures, sort options) |
| `settings.py` + env vars + Vault | Same code runs locally and in CI, no secrets in the repo |
| Trace + screenshot on failure | Debug CI failures without re-running |
| MCP at design time only | Tests stay deterministic; AI speeds up authoring |

## Likely questions
- **How do you avoid flaky tests?** Playwright auto-waits, stable selectors (data-test ids), independent tests, no sleeps. For bulk reads like `all_inner_texts()` I add an explicit wait.
- **How do you run on many browsers?** pytest-playwright runs each test per `--browser`; `--all-browsers` runs chromium, firefox and webkit.
- **How do you scale it?** `pytest-xdist` for parallel runs (`pytest -n 4`), markers to split smoke/regression, sharding in CI.
- **How do you share login across tests?** A `logged_in` fixture today; Playwright storage state (save once, reuse) as the next step.
- **Where would you add more?** Data factories, parallel runs, Allure report, Docker image, Slack notifications.
- **What does MCP do here?** Lets an AI assistant operate a real browser to find locators and draft tests. Human reviews everything; CI runs only committed code.
- **How are secrets handled?** Vault first, then env vars, then a default (public demo credentials only). GitHub secrets in CI.
