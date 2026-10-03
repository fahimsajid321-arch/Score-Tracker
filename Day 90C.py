import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)

# FIX 1: Correct BeautifulSoup initialization
soup = BeautifulSoup(response.text, "html.parser")

# FIX 2: Use BBC-specific headline elements (h2 tags)
headlines = soup.find_all("h2", attrs={"data-testid": "card-headline"})

print("--- BBC HEADLINES ---\n")

for idx, headline in enumerate(headlines[:5], 1):
    title = headline.text.strip()

    # Find the parent <a> tag to get the link
    parent_link = headline.find_parent("a")

    if parent_link:
        link = parent_link.get("href", "")
        # Handle relative links (e.g., /news/12345 -> https://www.bbc.com/news/12345)
        if link.startswith("/"):
            link = "https://www.bbc.com" + link

        print(f"{idx}. {title}")
        print(f"   Link: {link}\n")
        