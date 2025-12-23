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


👉 **Uwaga**: jeśli nazwa repo lub workflow się różni, badge URL musi się zgadzać dokładnie z:
`.github/workflows/tests.yml`

---