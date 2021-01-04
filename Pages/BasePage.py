from Configs import BaseConfig
from Locators import Common as Locator


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(BaseConfig.BASE_URL)
        popup = self.driver.find_elements_by_xpath(Locator.Notification_Popup_Xpath)
        if len(popup) > 0:
            popup[0].click()

    def get_title(self):
        return self.driver.title

