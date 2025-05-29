import requests
import json

with open("dailyData.json", "r") as file:
    topNewsToday = json.load(file)

#stores the date of the news publication
dailyDate = dict(topNewsToday['top_news'][0])['news'][0]['publish_date'][0:10]

#Stores a row of the news and the title for the day
dailyRow = ""

for i in range(10):
    dailyRow = dailyRow + str(dict(topNewsToday['top_news'][i])['news'][0]['id']) + "," + str(dict(topNewsToday['top_news'][i])['news'][0]['title']).replace(",","_") + ","
    #Appends the full articles to the newsFull.csv file
    with open("newsFull.csv", "a", encoding='utf-8') as g:
       g.write("\n" + str(dict(topNewsToday['top_news'][i])['news'][0]['id']) + "," + str(str(dict(topNewsToday['top_news'][i])['news'][0]['text']).replace(",","_")).replace("\n"," "))


#Appends the created daily row to the dailyNews.csv file
with open("dailyNews.csv", "a") as f:
  f.write("\n" + dailyDate + "," +  dailyRow[:-1])