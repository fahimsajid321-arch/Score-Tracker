import requests

# 1. Configuration
API_KEY = "d41e6a840cfb473092aa9a2505f8269c"  # Replace with your actual key
BASE_URL = "https://newsapi.org/v2/everything"

# 2. List of topics to query
topics = ["technology", "sports", "business"]

for topic in topics:
    # 3. Define parameter query mapping
    params = {
        "q": topic,  # The search term/topic
        "language": "en",  # Filter for English articles
        "sortBy": "publishedAt",  # Sort by newest articles
        "pageSize": 3,  # Limit results per topic
        "apiKey": API_KEY,
    }

    try:
        # 4. Execute HTTP GET request
        response = requests.get(BASE_URL, params)

        # Raise an exception for HTTP error statuses (4xx, 5xx)
        response.raise_for_status()

        data = response.json()
        articles = data.get("articles", [])

        print(f"\n================ TOPIC: {topic.upper()} ================")

        if not articles:
            print("No articles found.")
            continue

        for idx, article in enumerate(articles, 1):
            title = article.get("title", "No Title")
            source = article.get("source", {}).get("name", "Unknown Source")
            url = article.get("url", "No Link")

            print(f"{idx}. {title}")
            print(f"   Source: {source}")
            print(f"   URL: {url}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news for '{topic}': {e}")