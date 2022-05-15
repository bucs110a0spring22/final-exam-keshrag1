import locationAPI
import requests
import weatherAPI
def main():
  lapi = locationAPI.Location()
  info = lapi.get()
  #print(info)
  #print(type(info))
  #print(info['woeid'])
  wapi = weatherAPI.Weather()
  weather_data = wapi.get()
  precipitation = weather_data.get('weather_state_name')
  min_temp = weather_data.get('min_temp')
  max_temp = weather_data.get('max_temp')
  print(f' The weather is {precipitation}')
  print(f' The low is {min_temp} degrees celsius')
  print(f' The high is {max_temp} degrees celsius')
main()

