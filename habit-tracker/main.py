import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "jvk"
TOKEN = "adhg1445mnbmbsdq21"
today = datetime.now()
# print(today.strftime("%Y%m%d"))
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Exercise Graph",
    "unit": "Calories",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many calories did you burn today?"),
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)
pixel_update_endpoint = f"{pixel_endpoint}/20230521"

# response = requests.put(url=pixel_update_endpoint, json=pixel_config, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response.text)