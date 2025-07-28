from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
import os
import sys
import time

url = "http://ybt.ssoier.cn:8088/"
def to_URL(img_src, scheme="https"):
    if not img_src:
        return None
    if img_src.startswith("//"):
        return scheme + ":" + img_src
    return urljoin(url, img_src)
option = Options()
option.add_argument("--user-agent=Mozilla/5.0")
option.add_argument("--incognito")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=option)
driver.get(url)
driver.execute_script("""
    document.querySelector("a[href='javascript:void(0);'][onclick=\\"setCookie('xmenu','4,noippj')\\"]").click();
""")


try:
    driver.execute_script('document.querySelector(\'a[href="login0.php"]\').click();')
except Exception as e:
    print(f"login点击失败,原因:{e}")
    sys.exit(1)

try:
    driver.execute_script('document.querySelector(\'input[type="text"][name="username"]\').value = arguments[0];', "chenjilin")
except Exception as e:
    print(f"users失败,原因:{e}")
    sys.exit(1)

try:
    driver.execute_script('document.querySelector(\'input[type="password"][name="password"]\').value = arguments[0];', "Xg520530")
except Exception as e:
    print(f"pass失败,原因:{e}")
    sys.exit(1)

try:
    driver.execute_script('document.querySelector(\'input[name="login"][type="submit"]\').click();')
except Exception as e:
    print(f"login失败,原因:{e}")
    sys.exit(1)

time.sleep(2)
findlist = driver.find_elements(By.CSS_SELECTOR, 'td.xlist>a.list2_link')
option.add_argument("--headless")
os.makedirs("downloaded_problem", exist_ok=True)
for item in findlist:
    title = item.text
    href = item.get_attribute("href")
    path = to_URL(href)
    print(f"{title}: {to_URL(href)}")
    html = webdriver.Chrome(options=option)
    html.get(path)
    with open(f"downloaded_problem\\{title}.html","w",encoding="utf-8") as f:
        f.write(html.page_source)
    html.quit()
driver.quit()