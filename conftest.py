import pytest


@pytest.fixture(scope='session')
#request is used to return the parameter associated wth that testcase
def usercred(request):
    return request.param

@pytest.fixture(scope="function")
def browserInstance(playwright,request):
      # for golbal varaible
    browser_name= request.config.getoption("--browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "safari":
        browser = playwright.SafariWebDriver.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    yield page
    #yeild it will execute till yield and it will come back after executing and then execute after yeild
    context.close()
    browser.close()

# this will store the browser name, this is from the pytest
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store" ,default="chrome", help='Chrome or Firefox or Safari')
