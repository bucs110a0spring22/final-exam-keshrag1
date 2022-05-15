import requests
import locationAPI

class Weather():

  def __init__(self):
    """
     This function places the URL of the API into a variable, uses the where on Earth ID from the previous API to determine the location, and asks the user for the input date
    args: self(object) this is the Weather class
    returns: none
    """
    lapi = locationAPI.Location()
    info = lapi.get()
    locationID = (info.get('woeid')) #okay , no problem, take care, thanks for your help
    date = input('Enter a date in the format of yyyy/mm/dd: ')
    self.url =  f'https://www.metaweather.com/api/location/{locationID}/{date}'

  def get(self):
    """
     This function places the URL of the API into a variable and asks the user for input on which city they want to know the weather in
    args: self(object) this is the Weather class
    returns: Weather information of a city on a specific day(str), none
    """
    r = requests.get(self.url) #LocationID is empty. alright. Thank you very much!
    response = r.json()
    true = True
    if ('data' in response) or true == True:
      return response[0]
    else:
      return None