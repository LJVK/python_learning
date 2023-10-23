import requests
import os
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API_KEY = os.environ['TEQUILA_API_KEY']

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        # code = "TESTING"
        parameters = {
            "term" : city_name,
            "locale" : "en-US",
            "location_types" : "city",
            "limit" : 10,
        }
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        response = requests.get(url=TEQUILA_ENDPOINT, params=parameters, headers=headers)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]