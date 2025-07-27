from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import sys
import time


option = Options()
option.add_argument("--users-agent=mozilla/5.0")
option.add_argument("--incogrito")
option.add_experimental_option("excludeSwitches",["enable-automation"])
option.add_experimental_option("useAutomationExtension",False)
driver = webdriver.Chrome(options = option)
driver.get("https://vjudge.net/group")

login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a.nav-link.login[href="javascript:void(0)"]'))
)
time.sleep(2.34)
try:
    login.click()
except Exception as e:
    print(f"login点击失败,原因:{e}")
    sys.exit(1)

time.sleep(1.65)
try:
    driver.execute_script("document.getElementById('login-username').value = arguments[0];", "chen886")
except Exception as e:
    print(f"users失败,原因:{e}")
    sys.exit(1)

time.sleep(3.2312)
try:
    driver.execute_script("document.getElementById('login-password').value = arguments[0];", "568782")
except Exception as e:
    print(f"pass失败,原因:{e}")
    sys.exit(1)

time.sleep(20.9123)

try:
    driver.execute_script('document.queryselector("#btn-login")', "568782")
except Exception as e:
    print(f"login失败,原因:{e}")
    sys.exit(1)
driver.quit()
# <input type="checkbox">
# <span class="cb-i"></span>
# btn-login