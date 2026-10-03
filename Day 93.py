import requests
import json
Query = input("What type of news you want to read: ")
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-09-02&sortBy=publishedAt&apiKey=d41e6a840cfb473092aa9a2505f8269c"
r = requests.get(url)
# print(r.text)
response = json.loads(r.text)
# print(response)
for article in response["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------------------------------------------------")