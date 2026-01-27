from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
from bs4 import BeautifulSoup
import sys
import io

r = requests.get("https://yandex.ru/pogoda/ru/yuzhno-sakhalinsk/details/tomorrow?lat=46.95777&lon=142.729587")
r.encoding = 'windows-1251'
soup = BeautifulSoup(r.text, "html.parser")
day = soup.find_all('h3', class_='AppForecastDayHeader_dayTitle__23ecF')
day_time = soup.find_all('div', class_="AppForecastDayPart_caption__k1Uip AppForecastDayPart_center__esSb6")
temp = soup.find_all('div', class_="AppForecastDayPart_value__9pxTD AppForecastDayPart_center__esSb6 AppForecastDayPart_temp__kKbJG AppForecastDayPart_value__medium__JXTZV")
sky = soup.find_all('div', class_="AppForecastDayPart_caption__k1Uip AppForecastDayPart_center__esSb6 AppForecastDayPart_text__dFFbf AppForecastDayPart_showWide__hsoFN")
wind = soup.find_all('div', class_="AppForecastDayPart_value__9pxTD AppForecastDayPart_center__esSb6 AppForecastDayPart_wind__k3V5t")
morn_humidity = soup.find_all('div', class_="AppForecastDayPart_value__9pxTD AppForecastDayPart_center__esSb6 AppForecastDayPart_showNarrow__fTNAB", style='grid-area:m-hum')
sun_humidity = soup.find_all('div', class_="AppForecastDayPart_value__9pxTD AppForecastDayPart_center__esSb6 AppForecastDayPart_showNarrow__fTNAB", style='grid-area:d-hum')
even_humidity = soup.find_all('div', class_="AppForecastDayPart_value__9pxTD AppForecastDayPart_center__esSb6 AppForecastDayPart_showNarrow__fTNAB", style='grid-area:e-hum')
night_humidity = soup.find_all('div', class_="AppForecastDayPart_value__9pxTD AppForecastDayPart_center__esSb6 AppForecastDayPart_showNarrow__fTNAB", style='grid-area:n-hum')
humidity = []
for i in range(10):
    humidity.append(morn_humidity[i])
    humidity.append(sun_humidity[i])
    humidity.append(even_humidity[i])
    humidity.append(night_humidity[i])
# print(len(humidity))
class DayTimeForecast():
    def __init__(self):
        self.day_time = 0
        self.temp = 0
        self.sky = 0
        self.wind = 0
        self.humidity = 0

    def __str__(self):
        return f"{self.day_time} {self.temp} {self.sky} {self.wind}m/c {self.humidity}humidity "
class Forecast():
    def __init__(self):        
        self.day = 0
        self.morning = DayTimeForecast()
        self.sunset = DayTimeForecast()
        self.evening = DayTimeForecast()
        self.night = DayTimeForecast()

    def __str__(self):
        return f"{self.day}"


forecast_list = []
counter = 0
for i in day:
    forecast_list.append(Forecast())
    forecast_list[counter].day = i.text
    counter += 1
counter = 0

extra_list = []

day_time_forecast = []
for i in day_time:
    # forecast_list[counter].day_time = i.text
    extra_list.append(i.text)
    if len(extra_list) == 4:
        day_time_forecast.append(extra_list)
        extra_list = []
        
temp_forecast = []
for i in temp:
    extra_list.append(i.text)
    if len(extra_list) == 4:
        temp_forecast.append(extra_list)
        extra_list = []

sky_forecast = []
for i in sky:
    extra_list.append(i.text)
    if len(extra_list) == 4:
        sky_forecast.append(extra_list)
        extra_list = []

wind_forecast = []
for i in wind:
    extra_list.append(i.text)
    if len(extra_list) == 4:
        wind_forecast.append(extra_list)
        extra_list = []

humidity_forecast = []
for i in humidity:
    extra_list.append(i.text)
    if len(extra_list) == 4:
        humidity_forecast.append(extra_list)
        extra_list = []

# for i in day_time_forecast:
# print(day_time_forecast)
# print(len(day_time_forecast))
for i in day_time_forecast:
    obj = forecast_list[counter]
    obj.morning.day_time = i[0]
    obj.sunset.day_time = i[1]
    obj.evening.day_time = i[2]
    obj.night.day_time = i[3]
    counter += 1
counter = 0

for i in temp_forecast:
    obj = forecast_list[counter]
    obj.morning.temp = i[0]
    obj.sunset.temp = i[1]
    obj.evening.temp = i[2]
    obj.night.temp = i[3]
    counter += 1
counter = 0

for i in sky_forecast:
    obj = forecast_list[counter]
    obj.morning.sky = i[0]
    obj.sunset.sky = i[1]
    obj.evening.sky = i[2]
    obj.night.sky = i[3]
    counter += 1
counter = 0

for i in wind_forecast:
    obj = forecast_list[counter]
    obj.morning.wind = i[0]
    obj.sunset.wind = i[1]
    obj.evening.wind = i[2]
    obj.night.wind = i[3]
    counter += 1
counter = 0

# print(humidity_forecast)
for i in humidity_forecast:
    # print(counter)
    obj = forecast_list[counter]
    obj.morning.humidity = i[0]
    obj.sunset.humidity = i[1]
    obj.evening.humidity = i[2]
    obj.night.humidity = i[3]
    counter += 1
counter = 0

# class DayTimeForecast():
#     def __init__(self):
#         self.day_time = 0
#         self.temp = 0
#         self.sky = 0
#         self.wind = 0
#         self.humidity = 0
# class Forecast():
#     def __init__(self):        
#         self.day = 0
#         self.morning = DayTimeForecast()
#         self.sunset = DayTimeForecast()
#         self.evening = DayTimeForecast()
#         self.night = DayTimeForecast()

#     def __str__(self):
#         return f"{self.day}"
# print(f"forecast for next {len(forecast_list)} days")
text = ""
for i in forecast_list:
    text += f"""
    <div style='margin: 10px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;'>
        <h3 style='color: #2c3e50;'>{i.day}</h3>
        <div><b>🌅 Утро:</b> {i.morning}</div>
        <div><b>☀️ День:</b> {i.sunset}</div>
        <div><b>🌇 Вечер:</b> {i.evening}</div>
        <div><b>🌙 Ночь:</b> {i.night}</div>
    </div>"""

app = QApplication(sys.argv)

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(f'Прогноз погоды на {len(forecast_list)} дней')
        self.setGeometry(100, 100, 600, 700)
        label = QLabel(text=text)
        # codec = QTextCodec.codecForName("cp1251")
        # QTextCodec.setCodecForLocale(codec)
        layout = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setWidget(label)
        layout.addWidget(scroll)
        self.setLayout(layout)
window = WeatherApp()

window.show()

sys.exit(app.exec_())
