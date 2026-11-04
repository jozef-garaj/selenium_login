# selenium_login

[![Selenium Login Test](https://github.com/jozef-garaj/selenium_login/actions/workflows/selenium.yml/badge.svg)](https://github.com/jozef-garaj/selenium_login/actions/workflows/selenium.yml)

Selenium test that logs in to [saucedemo.com](https://www.saucedemo.com/) as `standard_user`
and checks that the **Products** page opens.

## Requirements

- Python 3.8+
- Firefox

Selenium 4.6+ downloads the matching geckodriver automatically (Selenium Manager).

## Run

```bash
pip install -r requirements.txt
python login_test.py
```

On success it prints `Login successful`; otherwise it fails with an `AssertionError`
or a `TimeoutException`.

To run without a visible browser window, set `MOZ_HEADLESS=1`.

## CI

GitHub Actions ([.github/workflows/selenium.yml](.github/workflows/selenium.yml)) runs the test
headless on every push and pull request to `main`, on the 1st and 15th of each month at 06:00 UTC (about every 2 weeks), and on demand
from the **Actions** tab (**Run workflow**).
