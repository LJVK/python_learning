import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "50d99ba620aebf87e37b1221f6ee4da1"
weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
will_rain = False
account_sid = os.environ['AC0746f4ee4cb56551fe19efda52aac230']
auth_token = os.environ['4d44462b352a3020909c7733bcdef3d1']

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, pls bring the umbrella.",
        from_='+15017122661',
        to='+18556409542'
    )

    print(message.sid)
