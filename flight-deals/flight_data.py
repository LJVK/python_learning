from data_manager import DataManager
from notification_manager import NotificationManager
import requests
import datetime
import os

FLIGHT_SEARCH_API = "https://api.tequila.kiwi.com/v2/search"
FLIGHT_SEARCH_API_KEY = os.environ['FLIGHT_SEARCH_API_KEY']
DATE_FROM = datetime.datetime.now() + datetime.timedelta(days=1)
FORMATTED_DATE_FROM = DATE_FROM.strftime("%d/%m/%Y")
DATE_TO = datetime.datetime.now() + datetime.timedelta(days=(6 * 30))
FORMATTED_DATE_TO = DATE_TO.strftime("%d/%m/%Y")
CONDITION_MET = False

class FlightData:
    # This class is responsible for structuring the flight data.

    def search_flights(self):
        global CONDITION_MET
        data_manager_instance = DataManager()
        notification_manager = NotificationManager()
        to_city_list = data_manager_instance.get_city_data()

        for city in to_city_list:
            to_city, lowest_flight_price = city
            # Initialize variables with default values
            departure_city_name = ""
            iata_from_airport = ""
            arrival_city_name = ""
            iata_to_airport = ""
            outbound_date = ""
            inbound_date = ""
            parameters = {
                "fly_from": "LON",
                "fly_to": to_city,
                "date_from": FORMATTED_DATE_FROM,
                "date_to": FORMATTED_DATE_TO
            }
            header = {
                "apikey": FLIGHT_SEARCH_API_KEY
            }
            response = requests.get(url=FLIGHT_SEARCH_API, params=parameters, headers=header)
            for row in response.json()['data']:
                flight_price = row['price']
                if flight_price < lowest_flight_price:
                    lowest_flight_price = flight_price
                    departure_city_name = row['cityFrom']
                    iata_from_airport = row['flyFrom']
                    arrival_city_name = row['cityTo']
                    iata_to_airport = row['flyTo']
                    outbound_date = row['local_departure'].split("T")[0]
                    inbound_date = row['local_arrival'].split("T")[0]
                    CONDITION_MET = True
            if CONDITION_MET:
                notification_manager.send_message(lowest_flight_price, departure_city_name, iata_from_airport,
                                                  arrival_city_name, iata_to_airport, outbound_date, inbound_date)
                CONDITION_MET = False
        return
