import requests
from bs4 import BeautifulSoup
data = {
    "username": "admin",
    "password": "123456"
}
response = requests.post("https://httpbin.org/post", data=data)
print(response.text)