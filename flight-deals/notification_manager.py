from twilio.rest import Client
import os


class NotificationManager():
    #This class is responsible for sending notifications with the deal flight details.
    # Download the helper library from https://www.twilio.com/docs/python/install
    import os

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    def send_message(self, lowest_flight_price, departure_city_name, iata_from_airport, arrival_city_name, iata_to_airport, outbound_date, inbound_date):
        twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
        twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(twilio_account_sid, twilio_auth_token)

        message = client.messages \
            .create(
            body=f"Sent from your Twilio account- Low Price alert! Only \xA3{lowest_flight_price} to fly from "
                 f"{departure_city_name}-{iata_from_airport} to {arrival_city_name}-{iata_to_airport}, "
                 f"from {outbound_date} to {inbound_date}",
            from_=os.environ['TWILIO_FROM_PHONE'],
            to=os.environ['TWILIO_TO_PHONE']
        )

        print(message.sid)