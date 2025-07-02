import time
import requests
import json
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

#checks if the stored date is the same as the current date and updates if not
def dayUpdateCheck(currDate):
    if str(currentStatus["day"]) != str(currDate):
        newStatusWrite = {"day": str(currDate), "acquiredStatus": "False"}
        with open("dataRetrieveStatus.json", "w") as file:
            newStatusWrite = json.dump(newStatusWrite, file)
        print("Day successfully updated \n")

#checks if conditions are correct for data grabbing and retreiving
def checkConditions(currDate, currHour, currStatus):
    if int(currHour) < 17:
        print("It's not yet at least 5pm EST.")
    elif currStatus == "True":
        print("Data was already captured and sent today.")
    else:
        newStatusWrite = {"day": str(currDate), "acquiredStatus": "True"}
        with open("dataRetrieveStatus.json", "w") as file:
            newStatusWrite = json.dump(newStatusWrite, file)
        print("Status successfully updated. \n")
        
        daysNews = topNews(currDate)
        dailyRow = ""

        for i in range(10):
            dailyRow = dailyRow + str(dict(daysNews['top_news'][i])['news'][0]['id']) + "," + str(dict(daysNews['top_news'][i])['news'][0]['title']).replace(",","_") + ","
            #Appends the full articles to the newsFull.csv file
            with open("newsFull.csv", "a", encoding='utf-8') as g:
                g.write("\n" + str(dict(daysNews['top_news'][i])['news'][0]['id']) + "," + str(str(dict(daysNews['top_news'][i])['news'][0]['text']).replace(",","_")).replace("\n"," "))

        #Appends the created daily row to the dailyNews.csv file
        with open("dailyNews.csv", "a") as f:
            f.write("\n" + currDate + "," +  dailyRow[:-1])
        
        print("Script successfully run. \n")


#stores date, military time, and military hour
currentDate = date.today()
currentTime = str(time.ctime())[-13:-5]
currentHour = currentTime[:2]


tillNextHour = currentTime[3:]
secondsTillNextHour = 3600 - (int(tillNextHour[:2])*60 + int(tillNextHour[3:]))

print("Today is: " + str(currentDate) + "\n")

with open("dataRetrieveStatus.json", "r") as file:
    currentStatus = json.load(file)

dayUpdateCheck(currentDate)

checkConditions(currentDate, currentHour, currentStatus["acquiredStatus"])

print("The current time is: " + currentTime)
print(str(secondsTillNextHour) + " seconds until the next hour.")
print("Aligning time now...")
time.sleep(secondsTillNextHour)

print("Time aligned.")

while True:
    currentTime = str(time.ctime())[-13:-5]
    print("The current time is: " + currentTime)
    currentHour = currentTime[:2]
    print("The hour is: " + currentHour + " O'clock")
    currentDate = date.today()


    dayUpdateCheck(currentDate)
    checkConditions(currentDate, currentHour, currentStatus["acquiredStatus"])

    print("All checks completed, syncing time")
    currentTime = str(time.ctime())[-13:-5]
    tillNextHour = currentTime[3:]
    secondsTillNextHour = 3600 - (int(tillNextHour[:2])*60 + int(tillNextHour[3:]))

    print("Time successfully synced, sleeping until " + str(int(currentHour) + 3) + " O'clock \n")
    time.sleep(secondsTillNextHour + 7200)
