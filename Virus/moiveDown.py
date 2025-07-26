import requests
from bs4 import BeautifulSoup
import os
import re
headers = {
    "User-Agent": "Mozilla/5.0"
}
url = "https://chatgpt.com/"
html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, "html.parser")
elements = soup.find_all("img")
os.makedirs("downloaded_imgs", exist_ok=True)
for index, item in enumerate(elements):
    imgurl = item.get("src")
    if not imgurl:
        continue
    if imgurl.startswith("//"):
        imgurl = "https:" + imgurl
    elif imgurl.startswith("/"):
        imgurl = url + imgurl  # 拼接域名
    img = requests.get(imgurl, headers=headers)
    filename = re.sub(r'[\\/:"*?<>|]+', "", os.path.basename(imgurl))
    if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
        filename += ".png"
    with open(f"downloaded_imgs/{index}_{filename}", "wb") as f:
        f.write(img.content)
    print(f"已保存: {filename},{imgurl}")
