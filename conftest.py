import pytest
from Data import Constants
from Utils.Utility import log
from Utils.WebdriverFactory import WebdriverFactory


@pytest.fixture()
def driver(request):
    log(Constants.TEST_START_LOG_MESSAGE.format(request.node.name))
    driver = WebdriverFactory().get_webdriver()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
    log(Constants.TEST_END_LOG_MESSAGE.format(request.node.name))
