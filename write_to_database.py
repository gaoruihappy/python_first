from dbwrite import *
from get import *
import time
location = 'beijing'
def getWeatherDate():
	time.sleep(5)	
	WeatherData = getweather(location)
	print(WeatherData)
	writeDataBase(WeatherData['HeWeather6'][0]);
def writeData():
	while True:
		getWeatherDate();
writeData()