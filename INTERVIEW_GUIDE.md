# How to explain this framework in an interview

## 30-second pitch
"It's a Python Playwright framework using pytest-bdd. Test cases are written in Gherkin so anyone can read them.
Each step calls a Page Object, and selectors live in a separate locators layer. It covers UI and API with the
same tool, produces HTML and Allure reports with screenshots and traces on failure, runs in GitHub Actions on
every push, and I use Playwright MCP with an AI assistant to explore pages, find locators and draft scenarios -
always reviewed by me before commit."

## The layers (draw this on the whiteboard)
```
Feature file (Gherkin)      "When the user logs in with ..."
        |
Step definition             tests/steps/*.py      - glue + assertions
        |
Page Object                 framework/pages/*.py  - user actions
        |
Locators                    framework/locators/*.py - selectors only
        |
Playwright -> browser / API
```
Rule of thumb: **locators = where, pages = how, steps = what + verify, features = why**.

## Design decisions and why
| Decision | Reason |
|---|---|
| Separate locators file | A UI change = a one-line fix in one place |
| No assertions in page objects | Pages stay reusable; the test decides pass/fail |
| pytest-bdd (not behave) | Reuses pytest fixtures, markers, plugins and pytest-playwright |
| Playwright for API too | One tool, one report, no extra library |
| Fixtures in conftest | Browser/API setup and cleanup are automatic |
| Tags -> markers (@smoke, @ui, @api) | Run subsets: `pytest -m smoke` in CI first |
| `settings.py` + env vars | Same code runs locally and in CI, no hardcoding |
| Trace + screenshot on failure | Debug CI failures without re-running |
| MCP at design time only | Tests stay deterministic; AI speeds up authoring |

## Likely questions
- **Why BDD?** Readable by non-technical people, living documentation, reusable steps. Don't over-use it: great for business flows, overkill for low-level checks.
- **How do you avoid flaky tests?** Playwright auto-waits, stable selectors (data-test ids), independent tests, no sleeps, traces to diagnose.
- **How do you scale it?** `pytest-xdist` for parallel runs (`pytest -n 4`), tags to split smoke/regression, sharding in CI.
- **How do you share login across tests?** Playwright storage state (save once, reuse), or API login then inject the token.
- **Where would you add more?** Test data factories, retries for known-flaky external calls, Allure history, Docker image, Slack notifications.
- **What does MCP do here?** Lets an AI assistant operate a real browser to find locators, draft Gherkin and debug failures. Human reviews everything; CI runs only committed code.
- **How are secrets handled?** Env vars locally, GitHub Actions secrets in CI. The demo credentials here are public.
