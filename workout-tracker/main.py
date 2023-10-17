import requests
from datetime import datetime
import os


# print(os.environ['WORKOUT_TRACKER_APP_ID'], os.environ['WORKOUT_TRACKER_APP_KEY'])
exercise_text = input("Tell me which exercise you did: ")
sheet_endpoint = "https://api.sheety.co/e26fd5fa58c680426c01ba9688c6e447/myWorkouts/workouts"
gender = "male"
weight = 80
height = 180
age = 30
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_header = {
    "x-app-id": os.environ['WORKOUT_TRACKER_APP_ID'],
    "x-app-key": os.environ['WORKOUT_TRACKER_APP_KEY']
}
parameters = {
    "query": exercise_text,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}
today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

response = requests.post(url=exercise_endpoint, json=parameters, headers=exercise_header)
response.raise_for_status()
result = response.json()["exercises"]

for exercise in result:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)