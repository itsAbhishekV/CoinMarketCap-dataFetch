from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {'start':'1',  'limit':'1',  'convert':'USD'}
headers = {'Accepts': 'application/json',  'X-CMC_PRO_API_KEY': '9c8e1437-807f-4aac-a733-7c2499937781'}
session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    new_data = data['data']
    print(new_data)
    # for i in range(0, len(new_data)):
    #     print(f"{new_data[i]['name']} ({new_data[i]['symbol']}) : {new_data[i]['quote']['USD']['price']} ")

except (ConnectionError, Timeout, TooManyRedirects) as e:  print(e)