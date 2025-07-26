import requests
from bs4 import BeautifulSoup
data = {
    "username": "chenjilin",
    "password": "Xg520530"
}
response = requests.post("http://oi.nks.edu.cn:19360/zh/Account/Login?returnurl=%2F", data=data)
print(response.text)