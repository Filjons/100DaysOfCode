from data_manager import DataManager
from flight_search import FlightSearch

fs = FlightSearch()

print(fs.get_iata("Paris"))


'''
m = DataManager()
data = m.get_data()['prices']
search = FlightSearch()

print(data)
new_data = []
updated_ind = []
for i in data:

    if i['iataCode'] == "":
        i['iataCode'] = search.get_iata(i['city'])
        new_data.append(i)
        updated_ind.append(i['id'])

print(new_data)

for i in new_data:
    for j in updated_ind:

        if i['id'] == j:
            b = {'price':i}
            print(m.put_data(body=b, row=j))
            '''
