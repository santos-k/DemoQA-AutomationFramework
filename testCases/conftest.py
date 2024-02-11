import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


base_url = "https://demoqa.com/"


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()


def pytest_addoption(parser):  # this will get the value from the CLI/Hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to the setup method
    return request.config.getoption("--browser")


# Pytest HTML Reports
# It is hooked for Adding Environment info to HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        config.stash[metadata_key]['Project Name'] = 'DemoQA Automation Framework'
        config.stash[metadata_key]['Module Name'] = 'DemoQA'
        config.stash[metadata_key]['Base URL'] = base_url
        config.stash[metadata_key]['Tester'] = 'Santosh Kumar'


# HTML Report title
def pytest_html_report_title(report):
    report.title = "DemoQA Test Framework!"


# It is hooked for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



