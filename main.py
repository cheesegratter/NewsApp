import requests
import json

with open("dailyData.json", "r") as file:
    topNewsToday = json.load(file)

dailySummary = []
for i in range(10):
    dailySummary.append(dict(topNewsToday['top_news'][i])['news'][0]['title'])

print(dailySummary)