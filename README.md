# Playwright + Pytest-BDD + Allure (Page Object Model)

## Structure
```
playwright_bdd_project/
├── conftest.py              # browser/page setup & teardown, failure screenshots, log attach
├── pytest.ini               # pytest + allure + logging config
├── requirements.txt
├── features/
│   ├── login.feature        # BDD scenarios (test data lives in Examples table)
│   └── steps/test_login_steps.py
├── pages/                   # Page Object Model
│   ├── base_page.py
│   ├── login_page.py        # #id (username), #pass (password)
│   └── dashboard_page.py    # get_by_text(..., exact=True) verification
├── utils/                   # config, logger, screenshot helper
├── logs/                    # automation.log, pytest.log
├── screenshots/             # PNGs (after login + on failure)
└── reports/                 # allure-results
```

## Setup
```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

## Configure
Set your login page URL (default is a placeholder):
```bash
export BASE_URL="https://your-app.com/login"     # Windows: set BASE_URL=...
```

## Run
```bash
pytest                                  # headless chromium
pytest --headed                         # see the browser
pytest --browser-name firefox
pytest -m login
```

## Allure report
Install the Allure CLI (https://allurereport.org/docs/install/), then:
```bash
allure serve reports/allure-results
# or generate static:
allure generate reports/allure-results -o reports/allure-report --clean
```

## Test data
| username | password    | title     |
|----------|-------------|-----------|
| prayash  | prayash@123 | Dashboard |
| Sahoo    | Sahoo@123   | Dashboard |

Edit the `Examples:` table in `features/login.feature` to change data.
