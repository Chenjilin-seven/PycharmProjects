import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin
headers = {
    "User-Agent": "Mozilla/5.0"
}
url = input("请输入网址:")
def to_URL(img_src, scheme="https"):
    if not img_src:
        return None
    if img_src.startswith("//"):
        return scheme + ":" + img_src
    return urljoin(url, img_src)
html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, "html.parser")
elements = soup.find_all("img")
os.makedirs("downloaded_imgs", exist_ok=True)
for index, item in enumerate(elements):
    imgurl = item.get("src")
    if not imgurl or imgurl.startswith("data:"):
        continue
    try:
        imgurl = to_URL(imgurl, "https")
        img = requests.get(imgurl, headers=headers)
        if img.status_code != 200:
            raise Exception(f"状态码: {img.status_code}")
    except Exception:
        try:
            imgurl = to_URL(imgurl, "http")
            img = requests.get(imgurl, headers=headers)
            if img.status_code != 200:
                raise Exception(f"状态码: {img.status_code}")
        except Exception as e:
            print(f"{imgurl} // error: {e}")
            continue

    filename = re.sub(r'[\\/:"*?<>|]+', "", os.path.basename(imgurl))
    if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
        filename += ".png"
    with open(f"downloaded_imgs/{index}_{filename}", "wb") as f:
        f.write(img.content)
    print(f"已保存: {filename}, 来自 {imgurl}")
