from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import requests, random, time, cv2, sys, os
from urllib.parse import urljoin

def extract_url(s):
    return s.split('"')[1] if '"' in s else s.split('(')[-1].split(')')[0]

def to_URL(img_src, scheme="https"):
    if img_src.startswith("//"):
        return scheme + ":" + img_src
    return urljoin(url, img_src)

def generate_track(distance):
    track = []
    current = 0
    mid = distance * 4/5
    t = 0.2
    v = 0
    while current < distance:
        a = random.uniform(2, 5) if current < mid else -random.uniform(3, 5)
        v0 = v
        v = v0 + a * t
        move = v0 * t + 0.5 * a * t * t
        current += move
        track.append(round(move))
    track += [-2, -1, 1]
    return track

url = "https://xxxxx"  # 请替换为真实地址
option = Options()
option.add_argument("--user-agent=Mozilla/5.0")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=option)
driver.get(url)
time.sleep(3)

bg_url = extract_url(driver.execute_script("return document.querySelector('.geetest_canvas_bg').style.backgroundImage"))
fullbg_url = extract_url(driver.execute_script("return document.querySelector('.geetest_canvas_fullbg').style.backgroundImage"))

requests.get(to_URL(bg_url)).content
with open("bg.png", "wb") as f:
    f.write(requests.get(to_URL(bg_url)).content)

with open("fullbg.png", "wb") as f:
    f.write(requests.get(to_URL(fullbg_url)).content)

bg = cv2.imread("bg.png", 0)
fullbg = cv2.imread("fullbg.png", 0)
result = cv2.matchTemplate(fullbg, bg, cv2.TM_CCOEFF_NORMED)
_, _, _, max_loc = cv2.minMaxLoc(result)
x_offset = max_loc[0] - 6

slider = driver.find_element(By.CLASS_NAME, "geetest_slider_button")
ActionChains(driver).click_and_hold(slider).perform()
track = generate_track(x_offset)
for x in track:
    ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
    time.sleep(0.015)
ActionChains(driver).release().perform()
