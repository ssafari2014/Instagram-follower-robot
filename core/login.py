"""عملکرد ورود به سیستم را مدیریت می‌کند"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def login(username, password):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)  # بستن خودکار نداشته باشه

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    # وارد کردن نام کاربری و رمز عبور
    driver.find_element(By.NAME, "username").send_keys(username)
    time.sleep(5)
    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, value="//*[@id='mount_0_0_2x']").click()
    time.sleep(5)

    return driver

