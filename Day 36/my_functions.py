
from datetime import date
import json
import requests
from get_stuff import get_stuff
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_FUNCTION = "TIME_SERIES_DAILY"


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
    diff_percentage = (diff / price_A) * 100
    return (diff_percentage)


def get_news():

    #DATE = date.today()
    DATE = '2024-08-08'
    API_KEY = get_stuff('newsapi_key')
    url = (
        f'https://newsapi.org/v2/everything?q=Tesla&language=en&from={DATE}&apiKey={API_KEY}')

    r = requests.get(url)
    data = r.json()
    #print(data['articles'][:3])
    
    return (data['articles'][:3])


def format_news(news=[]):
    news_list = []
    change = str(get_price_change()) + '\n'
    news_list.append(change)
    for i in range(len(news)):
        n = ''
        n += (str(news[i]['title']))
        n += '\n'
        n += (str(news[i]['description']))
        n += '\n'
        n += '\n'
        news_list.append(n)
    
    [print(n) for n in news_list]
