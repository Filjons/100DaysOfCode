from data_manager import DataManager
from flight_search import FlightSearch

m = DataManager()
data = m.get_data()['prices']
search = FlightSearch()

print(data)
new_data = []
for i in data:

    if i['iataCode'] == "":
        i['iataCode'] = search.get_iata(i['city'])
        new_data.append(i)

print(new_data)
