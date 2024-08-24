#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
m = DataManager()
data = m.get_data()['prices']
search = FlightSearch()

new_data = []
for i in data:

    if i['iataCode'] == "":
        i['iataCode'] = search.get_iata(i['city'])
        new_data.append(i)


