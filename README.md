# selenium_login

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
