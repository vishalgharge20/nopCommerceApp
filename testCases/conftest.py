from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from utilities.customLogger import LogGen


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
        print("********** Launching Chrome Browser **********")
    elif browser == "edge":
        driver = webdriver.Edge("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        print("********** Launching Edge Browser **********")
    else:
        driver = webdriver.Chrome("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    return driver


def pytest_addoption(parser):  # this will get the value from CLI/hook
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########## pytest html Report ##########

# it is hook for adding Environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Vishal'

# it is a hook to delete/modify environment info to html Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
    metadata.pop("Packages",None)
