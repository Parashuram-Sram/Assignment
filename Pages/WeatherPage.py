from Data import Constants
from Locators import Common as Locator
from Pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from Utils import Utility


class WeatherPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        sub_menu = self.driver.find_element_by_id(Locator.Sub_Menu_Id)
        sub_menu.click()
        element = self.driver.find_element_by_link_text(Locator.Section_Text)
        element.click()

    def pin_your_city(self, city):
        search_box = self.driver.find_element_by_id(Locator.Searchbox_Id)
        search_box.send_keys(city)
        city = self.driver.find_elements_by_id(city)
        if len(city) > 0:
            city = city[0]
            if city.is_selected():
                city.click()
            city.click()

    def city_information_from_map(self, city):
        elem = self.driver.find_element_by_xpath(Locator.City_Title_Xpath.format(city))
        return elem.get_attribute(Constants.TITLE_ATTR)

    def city_temperature_information_from_map(self, city):
        temp_red = self.driver.find_element_by_xpath(
            Locator.City_Temp_Xpath.format(city, Locator.Temperature_In_Celsius_Class))
        temp_white = self.driver.find_element_by_xpath(
            Locator.City_Temp_Xpath.format(city, Locator.Temperature_In_Fahrenheit_Class))

        return {
            Constants.CEL_CLASS: Utility.extract_temperature_from_text(temp_red.text),
            Constants.FAR_CLASS: Utility.extract_temperature_from_text(temp_white.text)
        }

    def get_city_temperature_information_from_map_by_unit(self, city, unit):
        self.pin_your_city(city)
        if unit == Constants.CEL_UNIT:
            elem = self.driver.find_element_by_xpath(
                Locator.City_Temp_Xpath.format(city, Locator.Temperature_In_Celsius_Class))
        else:
            elem = self.driver.find_element_by_xpath(
                Locator.City_Temp_Xpath.format(city, Locator.Temperature_In_Fahrenheit_Class))

        return float(Utility.extract_temperature_from_text(elem.text))

    def revealed_city_weather_details_from_map(self, city):
        elem_xpath = Locator.City_Title_Xpath.format(city)
        city = self.driver.find_element_by_xpath(elem_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(city).click().perform()
        popup = self.driver.find_elements_by_xpath(Locator.City_Weather_Popup_Xpath)
        return [itm.text for itm in popup]

    def get_pin_your_city_pane_header(self):
        elem = self.driver.find_element_by_class_name(Locator.Pin_Your_City_Class)
        return elem.text

    def get_reset_to_default_text(self):
        elem = self.driver.find_element_by_id(Locator.Reset_To_Default_Id)
        return elem.get_attribute(Constants.TITLE_ATTR)

    def click_reset_to_default_button(self):
        elem = self.driver.find_element_by_id(Locator.Reset_To_Default_Id)
        elem.click()

    def get_visible_pin_city_count(self):
        elem = self.driver.find_element_by_id(Locator.Visible_Cities_To_Pin_Group_Id)
        cities = elem.find_elements_by_class_name(Locator.Visible_City_To_Pin_Class)
        cities = [1 for city in cities if city.is_displayed()]
        return len(cities)

    def get_selected_city_count(self):
        elem = self.driver.find_element_by_id(Locator.Visible_Cities_To_Pin_Group_Id)
        cities = elem.find_elements_by_class_name(Locator.Visible_City_To_Pin_Class)

        cities = [1 for city in cities if city.find_element_by_tag_name(Locator.Input_Tag).is_selected()]
        return len(cities)
