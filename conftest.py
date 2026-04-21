import pytest
from selenium import webdriver
from config.settings import BASE_URL, USER_ID

"""
The driver fixture initializes the WebDriver, navigates to the specified URL with the user ID for authentication, and ensures that the browser is closed after the tests are completed.
"""

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL+"?user-id="+USER_ID)
    yield driver
    driver.quit()