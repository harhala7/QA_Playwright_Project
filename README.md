[![Playwright Tests](https://github.com/harhala7/QA_Playwright_Project/actions/workflows/tests.yml/badge.svg)](https://github.com/harhala7/QA_Playwright_Project/actions/workflows/tests.yml)

# Playwright Test Automation (Python)

End-to-end UI test automation project built with **Playwright (Python)** and **pytest**.
The project demonstrates stable UI testing, modern Playwright patterns and CI integration.

## Tech stack
- Playwright (Python)
- pytest
- GitHub Actions (CI)
- Chromium (headless)

## What is covered
- Page Object Model (Playwright-style, lightweight)
- Stable assertions with auto-waits
- Authentication via storage state (no repeated login)
- Screenshots, videos and traces on test failure
- CI pipeline running tests on every push and pull request

## Project structure
tests/
pages/
login_page.py
inventory_page.py
test_smoke.py
test_auth_setup.py


## Run tests locally
```bash
pip install -r requirements.txt
python -m playwright install
pytest

CI

Tests are executed automatically using GitHub Actions on every push and pull request.
On failure, Playwright artifacts (trace, screenshot, video) are available for debugging.

## Test suites
- Smoke tests: `tests/ui/test_smoke.py`
- Inventory tests: `tests/ui/test_inventory.py`
- Auth setup (storage state): `tests/auth/test_auth_setup.py`

## Run all:
```bash
pytest

## Run only smoke:
pytest -q tests/ui/test_smoke.py

## Run only inventory:
pytest -q tests/ui/test_inventory.py


## Storage state (authenticated session)

This project uses Playwright storage state to avoid logging in for every test.

## egenerate storage state:
pytest -q tests/auth/test_auth_setup.py

## The file is saved to:

artifacts/storage_state.json (ignored by git)

---