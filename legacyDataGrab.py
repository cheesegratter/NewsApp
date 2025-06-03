import requests
import json
import datetime
from datetime import date

for i in range(40):
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
    
    print(formattedDate)