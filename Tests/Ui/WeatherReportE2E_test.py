import pytest
from Apis.WeatherApi import WeatherApi
from Configs import BaseConfig
from Data import Constants,TestData
from Pages.WeatherPage import WeatherPage


@pytest.mark.usefixtures("driver")
class TestWeatherReportE2E:
    @staticmethod
    def get_weather_param_value_from_weather_details(weather_details,param):
        for attribute in weather_details:
            if attribute.find(param) != -1:
                attrib = attribute.split(":")[1]
        return float(attrib.strip(" %"))

    @pytest.mark.feature
    def test_e2e_celsius_temperature_variation(self):
        page = WeatherPage(self.driver)
        ui_value = page.get_city_temperature_information_from_map_by_unit(TestData.City_Name, Constants.CEL_UNIT)

        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.CEL_UNIT, BaseConfig.TOKEN)
        json_data = response.json()
        api_value = json_data["main"]["temp"]

        temperature_diff = abs(api_value - ui_value)
        assert temperature_diff <= TestData.Api_Ui_Temperature_Variation

    @pytest.mark.feature
    def test_e2e_fahrenheit_temperature_variation(self):
        page = WeatherPage(self.driver)
        ui_value = page.get_city_temperature_information_from_map_by_unit(TestData.City_Name, Constants.FAR_UNIT)

        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.FAR_UNIT, BaseConfig.TOKEN)
        json_data = response.json()
        api_value = json_data["main"]["temp"]

        temperature_diff = abs(api_value - ui_value)
        assert temperature_diff <= TestData.Api_Ui_Temperature_Variation

    @pytest.mark.regression
    def test_e2e_humidity_variation(self):
        page = WeatherPage(self.driver)
        page.pin_your_city(TestData.City_Name)
        weather_details = page.revealed_city_weather_details_from_map(TestData.City_Name)
        ui_value = TestWeatherReportE2E.get_weather_param_value_from_weather_details(weather_details, "Humidity")

        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.FAR_UNIT, BaseConfig.TOKEN)
        json_data = response.json()
        api_value = json_data["main"]["humidity"]

        temperature_diff = abs(api_value - ui_value)
        assert temperature_diff <= TestData.Api_Ui_Humidity_Variation
