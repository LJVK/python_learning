import requests
from pprint import pprint


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.destination_cities = []
        self.sheet_get_endpoint = 'https://api.sheety.co/08e5b77cd17f84b0925680730e67729d/flightDeals/prices'
        self.user_post_endpoint = 'https://api.sheety.co/08e5b77cd17f84b0925680730e67729d/flightDeals/users'

    def get_price_data(self):
        response = requests.get(url=self.sheet_get_endpoint)
        response.raise_for_status()
        self.destination_data = response.json()['prices']
        # pprint(self.destination_data)
        return self.destination_data

    def update_sheet_data(self, sheet_data):
        for row in sheet_data:
            sheet_put_endpoint = f'{self.sheet_get_endpoint}/{row["id"]}'
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            # print(new_data)
            response = requests.put(url=sheet_put_endpoint, json=new_data)
            response.raise_for_status()
            # print(response.text)

    def get_city_data(self):
        response = requests.get(url=self.sheet_get_endpoint)
        response.raise_for_status()
        for row in response.json()['prices']:
            city_data = (row['iataCode'], row['lowestPrice'])
            self.destination_cities.append(city_data)
        # print(self.destination_cities)
        return self.destination_cities

    def post_user_data(self, user_first_name, user_last_name, user_email_1):
        user_data = {
            "user": {
                "firstName": user_first_name,
                "lastName": user_last_name,
                "email": user_email_1
            }
        }
        response = requests.post(url=self.user_post_endpoint, json=user_data)
        response.raise_for_status()
        # print(response.json())
        return
