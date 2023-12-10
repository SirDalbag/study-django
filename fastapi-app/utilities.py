import requests
from bs4 import BeautifulSoup as bs
from collections import OrderedDict


class Weather:
    @staticmethod
    def get_weather():
        url = "https://weather.com/ru-RU/weather/tenday/l/Almaty+Kazakhstan?canonicalCityId=e25e2b869e6e01f6f1fa4ab6b563313212c9718a0d78156ed8014563ba77c7dc"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Error: %s" % response.status_code)
        soup = bs(response.text, "html.parser")
        dates = Weather.get_dates(soup)
        high_temps = Weather.get_high_temp(soup)
        low_temps = Weather.get_low_temp(soup)
        conditions = Weather.get_condition(soup)
        weather_data = []
        for date, high_temp, low_temp, condition in zip(
            dates, high_temps, low_temps, conditions
        ):
            weather_data.append(
                {
                    "date": date,
                    "high_temp": high_temp,
                    "low_temp": low_temp,
                    "condition": condition,
                }
            )
        return weather_data

    @staticmethod
    def get_dates(soup):
        class_ = "DailyContent--daypartDate--3VGlz"
        data = [x.text for x in soup.find_all("span", class_=class_)]
        return list(OrderedDict.fromkeys(data))

    @staticmethod
    def get_high_temp(soup):
        class_ = "DetailsSummary--highTempValue--3PjlX"
        return [x.text for x in soup.find_all("span", class_=class_)]

    def get_low_temp(soup):
        class_ = "DetailsSummary--lowTempValue--2tesQ"
        return [x.text for x in soup.find_all("span", class_=class_)]

    def get_condition(soup):
        class_ = "DetailsSummary--extendedData--307Ax"
        return [x.text for x in soup.find_all("span", class_=class_)]
