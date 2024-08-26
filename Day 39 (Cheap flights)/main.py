#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
m = DataManager()
data = m.get_data()['prices']
search = FlightSearch()

new_data = []
updated_ind = []
# Check if the entry has a IATA code, if not then use flightsearch gto get one for that city.
for i in data:

    if i['iataCode'] == "":
        i['iataCode'] = search.get_iata(i['city'])
        new_data.append(i)
        updated_ind.append(i['id'])
 #Update the flight ledger on sheety.
for i in new_data:
    for j in updated_ind:

        if i['id'] == j:
            b = {'price': i}
            print(m.put_data(body=b, row=j))
