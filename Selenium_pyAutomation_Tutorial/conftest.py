import pytest
from selenium import webdriver

from First_Automation_Tutorial.e_commerce.test_saucedemo import TestUrl
from First_Automation_Tutorial.utility_page.test_data import TestData


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_browsers(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver= webdriver.Edge()
    request.cls.driver = driver
    print("Browser: \t", request.param)
    #driver.get(TestData.Url)
    driver.get(TestUrl.Url)
    driver.maximize_window()
    yield
    print("Close Browser")
    driver.close()