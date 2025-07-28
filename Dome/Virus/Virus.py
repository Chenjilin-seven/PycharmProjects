import requests
from bs4 import BeautifulSoup
url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
for movie in soup.find_all("div", class_="hd"):
    title = movie.a.span.text
    print(title)
    link = movie.a["href"]
    print(link)
    print(f"{title} - {link}")