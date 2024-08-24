import requests
import json
from get_stuff import get_stuff


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.token = get_stuff('sheety')['token']
        self.id = get_stuff('sheety')['id']
        self.header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        self.url = f"https://api.sheety.co/{self.id}/flightDeals/prices"

    def get_data(self):
        data = requests.get(url=self.url, headers=self.header)
        return data.json()

    def put_data(self):
        data = requests.get(url=self.url, headers=self.header)
        return data.json()

    pass


if __name__ == "__main__":

    m = DataManager()
    print(m.get_data())
