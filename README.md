# Magento Account Creation and Login Automation

This repository contains a Selenium + Python automation framework using **Behave (BDD)** and **Page Object Model (POM)** to test account creation and login functionality on the [Magento demo website](https://magento.softwaretestingboard.com/).

---

## 🚀 Features

- ✅ BDD-style test case with `Behave`
- ✅ Selenium WebDriver automation
- ✅ Page Object Model structure
- ✅ Dynamic account creation using timestamped emails
- ✅ Login validation with the same account
- ✅ Automatic screenshot capture after account creation and login
- ✅ Cross-platform support (ChromeDriver managed by `webdriver-manager`)

---

## 🧪 Running the Tests

1. ✅ Install dependencies:

bash
pip install -r requirements.txt
✅ Run the test with Behave:

bash
Copy
Edit
behave
📸 Screenshots
Screenshots are automatically saved during the test:

After successful account creation:
screenshots/after_account_creation_<timestamp>.png

After successful login:
screenshots/after_login_<timestamp>.png

These can be used as proof of test execution.

📚 Tools Used
Selenium WebDriver

Python 3.12+

Behave (BDD)

WebDriver Manager

Page Object Model (POM)

✍️ Author
Nikita Bawage
Automation Test Engineer
Email: surawarnikita@gmail.com
GitHub: @Nikubawage
