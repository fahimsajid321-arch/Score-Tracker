import requests

API_KEY = "d41e6a840cfb473092aa9a2505f8269c"
BASE_URL = "https://newsapi.org/v2/everything"

topics = []
choice_News = input("What kind of news you want to watch:")
topics.append(choice_News)
for topic in topics:
    params = {
        "q" : topic,
        "language" : "en",
        "sortBy"   : "publishedAt",
        "pageSize" : 11,
        "apikey"   : API_KEY,
    }

    try:
        response = requests.get(BASE_URL, params)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])
        print(f"--------------TOPIC: {topic.upper()}-----------------")
        if not articles:
            print("Article not Found")
            continue
        for idx,article in enumerate(articles,1):
            title = article.get("title", "No title")
            source = article.get("source", {}).get("name", "Unknown Source")
            URL = article.get("url", "No Link")

            print(f"{idx}.              {title}")
            print(f"          Source:  {source}")
            print(f"          URL:      {URL}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news, '{topic}': {e}")
