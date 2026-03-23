import requests
import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv("api")
url = os.getenv("base_url")

params = {
    "startDate": "2016-01-01",
    "endDate": "2016-01-03",
    "api_key": api
}
response = requests.get(url=url,params=params)
data = response.json()

cleaned_datas = []
for i in range(2):
    cleaned_data = [data[i]['sepID'],data[i]['eventTime'],data[i]['instruments'],data[i]['submissionTime'],data[i]['versionId'],data[i]['linkedEvents'],
                    data[i]['sentNotifications']]


    cleaned_datas.append(cleaned_data)

for i in cleaned_datas:
    print(i)
print(cleaned_datas)
