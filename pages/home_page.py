from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 15).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        print("✅ Page fully loaded")

    def go_to_home_page(self):
        self.driver.get("https://magento.softwaretestingboard.com/")
        self.wait_for_page_load()

    def go_to_create_account(self):
        self.wait_for_page_load()
        # Ensure logo is clicked to reset any hover state (optional)
        try:
            logo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.logo"))
            )
            logo.click()
        except:
            pass

        sign_in_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='panel header']//a[contains(text(),'Create an Account')]"))
        )
        sign_in_link.click()
        print("✅ Navigated to Create Account page")

    def logout(self):
        self.wait_for_page_load()

        # Step 1: Click dropdown
        for attempt in range(3):
            try:
                dropdown = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "li.customer-welcome > span"))
                )
                dropdown.click()
                print(f"✅ Clicked dropdown on attempt {attempt + 1}")
                break
            except Exception as e:
                print(f"⚠️ Attempt {attempt + 1} to click dropdown failed: {e}")
                time.sleep(2)
        else:
            raise TimeoutException("❌ Could not click customer dropdown.")

        # Step 2: Click logout
        for attempt in range(3):
            try:
                logout = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "li.authorization-link > a"))
                )
                logout.click()
                print("✅ Successfully Logged Out")
                return
            except Exception as e:
                print(f"⚠️ Attempt {attempt + 1} to click logout failed: {e}")
                time.sleep(2)

        raise TimeoutException("❌ Could not click 'Sign Out' link.")

    def go_to_login(self):
        # Open new tab
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])

        self.driver.get("https://magento.softwaretestingboard.com/")
        self.wait_for_page_load()

        # Optional logo click to stabilize
        try:
            logo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.logo"))
            )
            logo.click()
        except:
            pass

        # Retry Sign In link click
        for attempt in range(3):
            try:
                sign_in = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]"))
                )
                sign_in.click()
                print("✅ Sign In link clicked")
                return
            except Exception as e:
                print(f"⚠️ Attempt {attempt + 1} failed: Sign In link not clickable\n{e}")
                time.sleep(2)

        raise TimeoutException("❌ Unable to click Sign In link after multiple retries")
    def is_user_logged_in(self):
        try:
            welcome_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "li.customer-welcome"))
            )
            return welcome_element.is_displayed()
        except:
            return False
