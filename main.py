import requests
import json

with open("dailyData.json", "r") as file:
    topNewsToday = json.load(file)

dailyDate = dict(topNewsToday['top_news'][0])['news'][0]['publish_date'][0:10]

dailyRow = ""

for i in range(10):
    dailyRow = dailyRow + str(dict(topNewsToday['top_news'][i])['news'][0]['id']) + "," + str(dict(topNewsToday['top_news'][i])['news'][0]['title']).replace(",","_") + ","
    with open("newsFull.csv", "a") as g:
       g.write("\n" + str(dict(topNewsToday['top_news'][i])['news'][0]['id']) + "," + str(dict(topNewsToday['top_news'][i])['news'][0]['text']).replace(",","_"))


with open("dailyNews.csv", "a") as f:
  f.write("\n" + dailyDate + "," +  dailyRow[:-1])