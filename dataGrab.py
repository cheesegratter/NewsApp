import requests
import json
from datetime import date

def my_custom_function():
    #takes token from hidden file
    with open("token/token.txt") as tokenKey:
        token = tokenKey.read()
    url = "https://api.worldnewsapi.com/top-news?source-country=us&language=en&date=" + str(date.today())
    api_key = token

    headers = {
        'x-api-key': token 
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

#stores API JSON and writes it to local files
topNews = my_custom_function()
with open("dailyData.json", "w") as file:
    json.dump(topNews, file)