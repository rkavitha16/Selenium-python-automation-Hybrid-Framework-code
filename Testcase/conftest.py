from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://in-en.flightnetwork.com/")
    driver.maximize_window()
    request.cls.driver = driver

    yield  # execution goes back to the test

    driver.quit()  # teardown after test completes
