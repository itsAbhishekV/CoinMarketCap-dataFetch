from requests import Session
import json

URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
params = {'start':'1',  'limit':'10',  'convert':'USD'} #change limits acc to your needs
headers = {'Accepts': 'application/json',  'X-CMC_PRO_API_KEY': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'}  #Your coin market cap api key here
session = Session()
session.headers.update(headers)

response = session.get(URL, params=params)
data = json.loads(response.text)
new_data = data['data']


for i in range(0, len(new_data)):
    print(f"{new_data[i]['name']} ({new_data[i]['symbol']}) : {new_data[i]['quote']['USD']['price']} ")
