import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language_name", action="store", default=None, help="choose browser language:")


@pytest.fixture(scope ="function")
def driver(request):
    user_language = request.config.getoption("language_name")
    options = Options()
    options.add_experimental_option("prefs", {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(options=options)
    print('\nstart browser for test')

    yield driver
    print("\nquit browser")
    driver.quit()

