from selenium import webdriver
import pytest

base_url = "https://demoqa.com/"


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(base_url)
    yield driver
    driver.quit()

