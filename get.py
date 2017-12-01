from urllib import request
import json
def getweather(location):
	url = 'https://free-api.heweather.com/s6/weather/now?location='+location+'&key=51acaad248b5438196b8caa828890885'
	with request.urlopen(url) as f:
		data = f.read()
	return json.loads(data.decode('utf-8'))


#str = WeatherData['HeWeather6'][0]['update']['loc']
#print(time.mktime(time.strptime(str,"%Y-%m-%d %H:%M")))
