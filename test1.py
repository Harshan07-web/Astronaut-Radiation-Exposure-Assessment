
import requests

api_key = ""
base_url = "https://api.nasa.gov/DONKI/SEP"

params = {
    "startDate": "2016-01-01",
    "endDate": "2016-01-03",
    "api_key": api_key
}

response = requests.get(base_url, params=params)
response.raise_for_status()

data = response.json()

print(len(data))
print(data[0])

