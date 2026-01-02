[![Playwright Tests](https://github.com/harhala7/QA_Playwright_Project/actions/workflows/tests.yml/badge.svg)](https://github.com/harhala7/QA_Playwright_Project/actions/workflows/tests.yml)

# Playwright Test Automation (Python)

End-to-end UI test automation project built with **Playwright (Python)** and **pytest**.  
The project demonstrates stable UI testing, modern Playwright patterns, and CI integration.

## Tech stack
- Playwright (Python)
- pytest
- GitHub Actions (CI)
- Chromium (headless)

## What is covered
- Page Object Model (lightweight, Playwright-style)
- Stable assertions with built-in auto-waits
- Authentication via storage state (no repeated login)
- Screenshots, videos, and traces on test failure
- CI pipeline running tests on every push and pull request

## Project structure
```text
tests/
  ui/
    test_smoke.py
    test_inventory.py
  auth/
    test_auth_setup.py
pages/
  login_page.py
  inventory_page.py
```

## Run tests locally
```bash
pip install -r requirements.txt
python -m playwright install
pytest
```

## CI

Tests are executed automatically using GitHub Actions on every push and pull request.
On failure, Playwright artifacts (trace, screenshot, video) are available for debugging.

## Test suites

- Smoke tests: `tests/ui/test_smoke.py`
- Inventory tests: `tests/ui/test_inventory.py`
- Auth setup (storage state): `tests/auth/test_auth_setup.py`

## Run all tests
```bash
pytest
```

## Run only smoke tests
```bash
pytest -q tests/ui/test_smoke.py
```

## Run only inventory tests
```bash
pytest -q tests/ui/test_inventory.py
```

## Storage state (authenticated session)

This project uses Playwright storage state to avoid logging in for every test.

## Regenerate storage state
```bash
pytest -q tests/auth/test_auth_setup.py
```

The file is saved to:
```bash
artifacts/storage_state.json
```
