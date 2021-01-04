from Utils.Utility import log
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Configs import BaseConfig
from Data import Constants


class WebdriverFactory:

    def __init__(self):
        self.browser = BaseConfig.BROWSER

    def get_webdriver(self):

        if self.browser == Constants.CHROME:
            return webdriver.Chrome(executable_path=ChromeDriverManager().install())

        if self.browser == Constants.EDGE:
            return webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

        log("Invalid browser name in configuration", "critical")
        raise Exception("No such browser ", self.browser)
