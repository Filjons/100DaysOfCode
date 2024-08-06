import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

API_FUNCTION = "TIME_SERIES_DAILY"

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)
with open("json_file.json", "w") as data_file:
    json.dump(new_data, data_file, indent=4)

with open("json_file.json", "r") as data_file:
    # Reading old data

    data = dict(json.load(data_file))
    print(type(data))
    print(data)
    # Update old data
    data.update(newer_data)
with open("json_file.json", "w") as data_file:
    # Save updated data
    json.dump(data, data_file, indent=4)
