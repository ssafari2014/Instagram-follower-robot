# core/search.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_for_element(driver, xpath, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

def search(driver, keyword):
    try:
        # تلاش برای پیدا کردن مستقیم input سرچ
        search_input_xpath = "//input[@placeholder='Search']"
        search_input = wait_for_element(driver, search_input_xpath)
    except:
        # اگر نبود، اول روی آیکن اکسپلور کلیک کن
        explore_icon_xpath = "//a[contains(@href,'/explore/')]"
        wait_for_element(driver, explore_icon_xpath).click()
        time.sleep(2)
        search_input = wait_for_element(driver, "//input[@placeholder='Search']")

    # وارد کردن کلمه کلیدی برای سرچ
    search_input.clear()
    search_input.send_keys(keyword)
    time.sleep(3)  # صبر برای ظاهر شدن نتایج
