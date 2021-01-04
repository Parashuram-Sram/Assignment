from Data import TestData
from Utils.Utility import send_request
from Configs import BaseConfig


class WeatherApi:

    @staticmethod
    def get_weather_data_for_city(city, unit, token):
        url = BaseConfig.BASE_API_URL
        params = {
            'id': TestData.City_Id_Map[city],
            'appid': token,
            'units': unit
        }

        response = send_request(url, params)
        return response

