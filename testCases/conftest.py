import os
from datetime import datetime

import pytest
import pytest_html
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

base_url = "https://demoqa.com/"


@pytest.fixture()
def setup(browser):
    global driver  # this for taking screenshot
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extra", [])
    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            current_date = datetime.now().strftime("%Y-%m-%d")
            file_path = f"C:\Automation\Python\DemoQA-Automation\Screenshots\Failed_Screenshot_{current_time}.png"
            driver.get_screenshot_as_file(file_path)
            extra_html = f'<div><img src="{file_path}" style="width:250px;height:180px;" onclick="window.open(this.src)" align="right"/></div>'
            extras.append(pytest_html.extras.html(extra_html))
        report.extra = extras
