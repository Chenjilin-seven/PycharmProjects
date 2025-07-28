from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--headless")  # 无界面
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.get("https://movie.douban.com/top250")

time.sleep(3)  # 等待 JS 渲染完成

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

for movie in soup.select("div.item"):
    title = movie.find("span", class_="title").text
    rating = movie.find("span", class_="rating_num").text
    print(f"{title} - 评分: {rating}")

driver.quit()
