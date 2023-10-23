#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

sheet_data = data_manager.get_price_data()
# print(sheet_data)
# print(sheet_data[0]['iataCode'])
# print(sheet_data[0]['city'])
for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.get_destination_code(row['city'])

print(f"Sheet Data: \n {sheet_data}")
data_manager.update_sheet_data(sheet_data)
# data_manager.destination_data = sheet_data
# data_manager.update_sheet_data()
flight_data.search_flights()

