import pytest
import os
from datetime import datetime
from selenium import webdriver
from utils.logger import setup_logger, log_test_info

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    log_dir = "Logs"
    os.makedirs(log_dir, exist_ok=True)
    log_filename = datetime.now().strftime("%H%M%S_%d%m%Y") + ".txt"
    log_path = os.path.join(log_dir, log_filename)
    setup_logger(log_path)

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        test_comment = item.function.__doc__ or "Без комментария"
        log_test_info(item.name, report.outcome, report.duration, test_comment)

        if report.failed:
            os.makedirs("creenshoots", exist_ok=True)
            screenshot_path = os.path.join("creenshoots", f"{item.name}.png")
            try:
                driver = item.funcargs["browser"]
                driver.save_screenshot(screenshot_path)
            except Exception as e:
                print(f"Не удалось сохранить скриншот: {e}")
