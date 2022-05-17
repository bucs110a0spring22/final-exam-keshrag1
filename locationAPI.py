import requests

class Location:
  def __init__(self):
    '''
    This function places the URL of the API into a variable and asks the user for input on which city they want to know the weather in
    args: self(object) this is the Location class
    returns: none
    '''
    city = input('Enter the name of a major city such as New York, London, and Hong Kong: ')
    self.url = f'https://www.metaweather.com/api/location/search/?query={city}'
  def get(self):
    """
     This function retrieves data from the API URL
    args: self(object) this is the Location class
    returns: The data on the city enterd by the user(str), none
    """
    r = requests.get(self.url)
    response = r.json()
    true = True
    if ('data'in response) or true == True:
      return response[0]
    else:
      return None
  