import requests
from bs4 import BeautifulSoup

# Send a request directly to Dawn's Tech category
url = "https://www.dawn.com/tech"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find article headline tags on Dawn
articles = soup.find_all("article", class_="story")

print("--- Latest Tech Headlines from Dawn News ---\n")

for idx, article in enumerate(articles[:5], 1):
    # Get headline text inside the <a class="story__link"> tag
    title_tag = article.find("a", class_="story__link")
    
    if title_tag:
        title = title_tag.text.strip()
        link = title_tag["href"]
        print(f"{idx}. {title}")
        print(f"   Link: {link}\n")