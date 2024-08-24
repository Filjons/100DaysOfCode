import requests
import json
from get_stuff import get_stuff


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:

        self.token = get_stuff('amadeus')['token']
        self.id = get_stuff('amadeus')['id']
        self.header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        self.url = f"https://api.sheety.co/{self.id}/flightDeals/prices"
        pass

    def get_iata(self, destination=""):
        return "TESTING"
        

    pass
