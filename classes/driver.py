# Photo girl: /html/body/div[2]/div/div[2]/div/div/section/div/div/div/div/div/div[3]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]
# //*[@id="current-card"]/div/div[1]/div[1]/img

# Description girl: /html/body/div[2]/div/div[2]/div/div/section/div/div/div/div/div/div[3]/div/div[2]/div/div/div/section[2]/div[2]/div/div
# //*[@id="main"]/div/div[3]/div/div[2]/div/div/div/section[2]/div[2]/div/div

import json
import os
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv

load_dotenv()

def get_random_chrome_user_agent():
    user_agent = UserAgent(browsers='chrome', os='windows', platforms='pc')
    return user_agent.random

def create_driver(user_id=1):
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_directory = os.path.join(script_dir, 'users')
    user_directory = os.path.join(base_directory, f'user_{user_id}')

    options.add_argument(f'user-data-dir={user_directory}')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--no-sandbox')
    # options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    ua = get_random_chrome_user_agent()
    stealth(driver=driver,
            user_agent=ua,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            run_on_insecure_origins=True
            )

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
      '''
    })


    return driver


def main_login(user_id=1):
    driver = create_driver(user_id)
    driver.get("https://vk.com/dating")

    driver.find_element(by=By.XPATH, value='//*[@id="quick_login"]/button[1]').click()
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='//*[@id="START_QR_PAGE"]/div/div[2]/div/button[1]').click()
    time.sleep(5)
    input_number = driver.find_element(by=By.XPATH, value='//*[@id="ENTER_LOGIN_PAGE"]/div/form/div[1]/div[3]/span/div/div[2]/input')
    input_number.click()

    input_number.send_keys(str(os.getenv("NUMBER_PHONE")))
    time.sleep(5)
    
    input_number.send_keys(Keys.ENTER) 
    time.sleep(20)
    time.sleep(300)
    with open("cookies.json", "w+", encoding="utf-8") as file:
        json.dump(driver.get_cookies(), file, indent=4, ensure_ascii=False)

def main_bot(user_id=1):
    driver = create_driver(user_id)
    with open("cookies.json", "r", encoding="utf-8") as file:
        for cookie in list(json.load(file)):
            try:
                driver.add_cookie(cookie)
                print(f"[+] {cookie["name"]} {cookie["domain"]}")
            except:
                print(f"[!] {cookie["name"]} {cookie["domain"]}")
    driver.get("https://vk.com/dating")

    

    return driver

if __name__ == "__main__":
    main_bot()