import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()