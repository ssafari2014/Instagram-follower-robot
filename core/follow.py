"""کاربران زیر را مدیریت می‌کند"""

# core/follow.py
from selenium.webdriver.common.by import By
import time

def follow_users(driver, count=10):
    time.sleep(3)
    links = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")
    post_links = [link.get_attribute('href') for link in links[:count]]

    for link in post_links:
        driver.get(link)
        time.sleep(3)
        try:
            follow_btn = driver.find_element(By.XPATH, "//button[text()='Follow']")
            follow_btn.click()
            print("✅ Followed one user")
            time.sleep(3)
        except:
            print("❌ Already followed or button not found")
            continue

