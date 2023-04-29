import smtplib
import time
import requests
from datetime import datetime

MY_LAT = 47.606209
MY_LNG = -122.332069
MY_EMAIL = "ljvk89@gmail.com"
MY_PASSWORD = "trefhkwybcuykyaa"


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG <= longitude <= MY_LNG:
        return True


def is_night():
    parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg="Subject: Look Up\n\n ISS is above you pls look into the sky")
