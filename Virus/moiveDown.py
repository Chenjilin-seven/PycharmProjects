import requests
from bs4 import BeautifulSoup
img_url = "https://example.com/logo.png"
response = requests.get(img_url)
with open("logo.png", "wb") as f:
    f.write(response.content)
