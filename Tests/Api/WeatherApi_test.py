import sys
from collections import Counter
import pytest
from Utils.Utility import log
from Apis.WeatherApi import WeatherApi
from Configs import BaseConfig
from Data import TestData, Constants
from Utils import Utility


class TestWeatherApi:
    @pytest.mark.regression
    def test_weather_api_response_payload(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.CEL_UNIT, BaseConfig.TOKEN)

        assert response.status_code == 200
        json_data = response.json()
        api_attributes = json_data.keys()

        assert Counter(api_attributes) == Counter(TestData.Weather_ApiData_For_City_Attributes)
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_city_temperature_in_celsius(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.CEL_UNIT, BaseConfig.TOKEN)

        assert response.status_code == 200
        json_data = response.json()

        assert Utility.is_valid_number(json_data["main"]["temp"])
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_city_temperature_in_fahrenheit(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.FAR_UNIT, BaseConfig.TOKEN)

        assert response.status_code == 200
        json_data = response.json()

        assert Utility.is_valid_number(json_data["main"]["temp"])
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_city_humidity(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.FAR_UNIT, BaseConfig.TOKEN)

        assert response.status_code == 200
        json_data = response.json()

        assert Utility.is_valid_number(json_data["main"]["humidity"])
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_city_wind_speed(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.FAR_UNIT, BaseConfig.TOKEN)

        assert response.status_code == 200
        json_data = response.json()

        assert Utility.is_valid_number(json_data["wind"]["speed"])
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_city_id(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.FAR_UNIT, BaseConfig.TOKEN)

        assert response.status_code == 200
        json_data = response.json()

        assert json_data["id"] == TestData.City_Id_Map[TestData.City_Name]
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_city_name(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.FAR_UNIT, BaseConfig.TOKEN)

        assert response.status_code == 200
        json_data = response.json()

        assert json_data["name"] == TestData.City_Name
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_city_latitude_longitude(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.FAR_UNIT, BaseConfig.TOKEN)

        assert response.status_code == 200
        json_data = response.json()

        assert Utility.is_valid_number(json_data["coord"]["lat"])
        assert Utility.is_valid_number(json_data["coord"]["lon"])
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_invalid_city_response_payload(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.Invalid_City_Name, Constants.FAR_UNIT,
                                                        BaseConfig.TOKEN)

        assert response.status_code == 404
        json_data = response.json()
        api_attributes = json_data.keys()

        assert Counter(api_attributes) == Counter(TestData.Invalid_ApiData_Response_Attributes)
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_invalid_city_response_message(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.Invalid_City_Name, Constants.FAR_UNIT,
                                                        BaseConfig.TOKEN)

        assert response.status_code == 404
        json_data = response.json()

        assert json_data["message"] == TestData.Invalid_City_Response_Message
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_invalid_apikey_response_payload(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.CEL_UNIT,
                                                        TestData.Invalid_Api_Key)

        assert response.status_code == 401
        json_data = response.json()
        api_attributes = json_data.keys()

        assert Counter(api_attributes) == Counter(TestData.Invalid_ApiData_Response_Attributes)
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))

    @pytest.mark.regression
    def test_weather_api_invalid_apikey_response_message(self):
        log(Constants.TEST_START_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
        response = WeatherApi.get_weather_data_for_city(TestData.City_Name, Constants.FAR_UNIT,
                                                        TestData.Invalid_Api_Key)

        assert response.status_code == 401
        json_data = response.json()

        assert json_data["message"] == TestData.Invalid_Api_Key_Response_Message
        log(Constants.TEST_END_LOG_MESSAGE.format(sys._getframe().f_code.co_name))
