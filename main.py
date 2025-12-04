import time
from classes.driver import main_bot
from selenium.webdriver.common.by import By

def main():
    pass

if __name__ == "__main__":
    driver = main_bot()

    while True:
        photo_girl = driver.find_element(by=By.XPATH, value='//*[@id="current-card"]/div/div[1]/div[1]/img')
        title_girl = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[3]/div/div[2]/div/div/div/section[1]/div[1]/div')
        description_girl = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[3]/div/div[2]/div/div/div/section[2]/div[2]/div/div')
        name_girl = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[3]/div/div[2]/div/div/div/section[1]/span/div/div[2]/div/div/div[1]')
        age_girl = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[3]/div/div[2]/div/div/div/section[1]/span/div/div[2]/div/div/span')
        
        button_dislike = driver.find_element(by=By.XPATH, value='//*[@id="current-card"]/div/div[2]/div/div[2]/div[2]/div/div[1]/span')
        button_like = driver.find_element(by=By.XPATH, value='//*[@id="current-card"]/div/div[2]/div/div[2]/div[2]/div/div[3]/span')

        
        time.sleep(5)


