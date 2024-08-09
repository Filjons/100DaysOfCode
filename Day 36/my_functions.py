from secret_stuff import API_KEY_NEWSAPI
from datetime import date
import requests
import json
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_FUNCTION = "TIME_SERIES_DAILY"


API_KEY = API_KEY_NEWSAPI

# Returns the change of the stock price in percentage.


def get_price_change():
    '''
    Get the price data API call
    replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    '''

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()

    # Retrive the closing price for yesterday and the day before
    key_Z = 'Time Series (Daily)'
    keys = data[key_Z].keys()

    key_A = list(keys)[0]
    key_B = list(keys)[1]

    price_A = float(data[key_Z][key_A]['4. close'])
    price_B = float(data[key_Z][key_B]['4. close'])

    diff = abs(price_A - price_B)
    change = 100*(diff / price_A)
    return (change)


def get_news():

    DATE = date.today()

    url = (f'https://newsapi.org/v2/top-headlines?q=Tesla&language=en&from={DATE}&apiKey={API_KEY}')

    r = requests.get(url)

    return(r.json()['articles'])


def print_news(news=None):

    head_lines = news[:3]

    print(head_lines)


