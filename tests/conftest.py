from distutils.log import error
from email.policy import default
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name" , action="store" , default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = Chrome(options=opts)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://app.rectangled.in/login")
    request.cls.driver = driver
    yield #excuted last
    # driver.close()
    