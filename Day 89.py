import requests
from bs4 import BeautifulSoup
# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
# r = requests.get(url)
# # print(r.text)

# soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
# for heading in soup.find_all("h3"):
#     print(heading)
import requests

url = "https://jsonplaceholder.typicode.com/users"
r = requests.get(url)

# 1. Check if the request was successful
r.raise_for_status()

# 2. Parse the JSON response into Python lists/dictionaries
users = r.json()

list_users = []

# 3. Iterate through each user dictionary
for user in users:
    # Safely get the company catchphrase
    catchphrase = user["company"]["catchPhrase"].lower()

    # 4. Check if "revolution" or "empower" is in the catchphrase
    if "revolution" in catchphrase or "empower" in catchphrase:
        list_users.append(
            {
                "Name": user["name"],
                "Email": user["email"],
                "Company": user["company"]["name"],
            }
        )

# 5. Output the results
for item in list_users:
    print(f"Name:    {item["Name"]}")
    print(f"Email:   {item['Email']}")
    print(f"Company: {item['Company']}")
    print("-" * 30)