"""نقطه ورودی برنامه شما که در آن ربات خود را راه‌اندازی و اجرا می‌کنید."""

from core.login import login
from core.search import search
from core.follow import follow_users

if __name__ == "__main__":
    driver = login("username", "password")
    search(driver, "python")
    follow_users(driver, count=5)