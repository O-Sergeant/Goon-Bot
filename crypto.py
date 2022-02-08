
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

baseurl = 'https://pro-api.coinmarketcap.com'
endpoint_listing_latest = '/v1/cryptocurrency/listings/latest'
endpoint_quotes_latest = '/v1/cryptocurrency/quotes/latest'
endpoint_map = '/v1/cryptocurrency/map'

parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f7e49c8e-7e10-472f-afe9-78a73ddc12ab',
}

session = Session()
session.headers.update(headers)

def make_request(url,endpoint,parameters):
  try:
    full = url + endpoint

    response = session.get(full, params=parameters)
    data = json.loads(response.text)
    #print (data)
    return data
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

def price(id):

  params = {
  'id': id,
}
  j = make_request(baseurl, endpoint_quotes_latest, params)
  #print(j['data'])
  price = j['data']['{}'.format(id)]["quote"]["USD"]["price"]
  return price


def coin_list(symbol):
  j = make_request(baseurl, endpoint_map, {'symbol': symbol})
  return j

