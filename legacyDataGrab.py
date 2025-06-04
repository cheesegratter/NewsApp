import requests
import json
import datetime
from datetime import date

def topNews(formatedDayData):
    #takes token from hidden file
    with open("token/token.txt") as tokenKey:
        token = tokenKey.read()
    url = "https://api.worldnewsapi.com/top-news?source-country=us&language=en&date=" + formatedDayData
    api_key = token

    headers = {
        'x-api-key': token 
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

# As there are only 50 requests that can be made a day, this loop runs 40 times
for e in range(40):
    #Loads the json file, stores counter data, then updates the counter for the next day
    with open("legacyDataCounter.json", "r") as file:
        legacyData = json.load(file)

    dayNum = legacyData['day']
    year = legacyData['year']
    dayOne = date(year,1,1)
    dayDate = dayOne + datetime.timedelta(days=int(dayNum))
    formattedDate = str(dayDate)

    dayNum = dayNum + 1
    if dayNum == 365:
        dayNum = 0
        year = year + 1

    newDayData = {"year" : year, "day" : dayNum}

    with open("legacyDataCounter.json", "w") as file:
        newDayData = json.dump(newDayData, file)
    
    # The following code combines the functions of dataGrab.py and dataWrite.py, reference those comments for functionality insights
    legacyNews = topNews(formattedDate)
    dailyRow = ""

    for i in range(10):
        dailyRow = dailyRow + str(dict(legacyNews['top_news'][i])['news'][0]['id']) + "," + str(dict(legacyNews['top_news'][i])['news'][0]['title']).replace(",","_") + ","
        #Appends the full articles to the newsFull.csv file
        with open("newsFull.csv", "a", encoding='utf-8') as g:
            g.write("\n" + str(dict(legacyNews['top_news'][i])['news'][0]['id']) + "," + str(str(dict(legacyNews['top_news'][i])['news'][0]['text']).replace(",","_")).replace("\n"," "))


    #Appends the created daily row to the dailyNews.csv file
    with open("dailyNews.csv", "a") as f:
        f.write("\n" + formattedDate + "," +  dailyRow[:-1])