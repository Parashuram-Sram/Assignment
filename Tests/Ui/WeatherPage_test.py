import pytest
from Data import Constants, TestData
from Pages.WeatherPage import WeatherPage
from Utils import Utility


@pytest.mark.usefixtures("driver")
class TestWeatherPage:

    @pytest.mark.feature
    def test_weather_page_pinned_city_details(self):
        city_name = TestData.City_Name
        page = WeatherPage(self.driver)
        page.pin_your_city(city_name)
        assert page.city_information_from_map(city_name) == city_name

    @pytest.mark.feature
    def test_weather_page_city_temperature_information(self):
        city_name = TestData.City_Name
        page = WeatherPage(self.driver)
        page.pin_your_city(city_name)
        temperature_info = page.city_temperature_information_from_map(city_name)
        assert Utility.is_valid_number(temperature_info[Constants.CEL_CLASS])
        assert Utility.is_valid_number(temperature_info[Constants.FAR_CLASS])

    @pytest.mark.feature
    def test_weather_page_revealed_details(self):
        city_name = TestData.City_Name
        page = WeatherPage(self.driver)
        page.pin_your_city(city_name)
        weather_details = page.revealed_city_weather_details_from_map(city_name)
        for attribute in weather_details:
            actual_item = attribute.split(":")[0]
            assert actual_item in TestData.Weather_Information_Attributes

    @pytest.mark.regression
    def test_weather_page_title(self):
        page = WeatherPage(self.driver)
        weather_page_title = page.get_title()
        assert weather_page_title == TestData.Weather_Page_Title

    @pytest.mark.regression
    def test_weather_page_pin_your_city_pane_header(self):
        page = WeatherPage(self.driver)
        pin_your_city_pane_header = page.get_pin_your_city_pane_header()
        assert pin_your_city_pane_header == TestData.Weather_Page_Pin_City_Pane_Header

    @pytest.mark.regression
    def test_weather_page_reset_to_default_text(self):
        page = WeatherPage(self.driver)
        reset_to_default_text = page.get_reset_to_default_text()
        assert reset_to_default_text == TestData.Weather_Page_Reset_To_Default_Text

    @pytest.mark.regression
    def test_weather_page_reset_to_default_cities(self):
        page = WeatherPage(self.driver)
        default_selected_count = page.get_selected_city_count()
        page.pin_your_city(TestData.City_Name)
        selected_count_after_city_pin = page.get_selected_city_count()
        assert default_selected_count + 1 == selected_count_after_city_pin
        page.click_reset_to_default_button()
        selected_count_after_reset = page.get_selected_city_count()
        assert default_selected_count == selected_count_after_reset

    @pytest.mark.regression
    def test_weather_page_pin_city_default_count(self):
        page = WeatherPage(self.driver)
        visible_pin_cities_count = page.get_visible_pin_city_count()
        assert visible_pin_cities_count == TestData.Visible_Pin_Cities_Count

    @pytest.mark.regression
    @pytest.mark.parametrize("city,count", [('Pune', 1), ('SomeCity', 0)])
    def test_weather_page_visible_cities_count_after_city_search(self, city, count):
        page = WeatherPage(self.driver)
        page.pin_your_city(city)
        visible_pin_cities = page.get_visible_pin_city_count()
        assert visible_pin_cities == count
