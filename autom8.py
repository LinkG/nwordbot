from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from random_word import RandomWords
import random

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

r = RandomWords()

driver.get('https://discord.com/channels/846425286765314088/853182317911343154')
time.sleep(30)
driver.implicitly_wait(20)
print('Here')
spam_xpath = ['//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]/div']

i=0
while True:
    driver.implicitly_wait(5)
    spam = driver.find_element_by_xpath(spam_xpath[0])
    spam.click()
    if i%10 == 0:
        spam.send_keys('p!boobs')
    elif i%5 == 0:
        spam.send_keys('p!butt')
    else:
        x = r.get_random_words(hasDictionaryDef='true', limit=5)
        while x is None:
            x = r.get_random_words(hasDictionaryDef='true', limit=5)
        spam.send_keys(' '.join(x))
    driver.implicitly_wait(1)
    spam.send_keys(Keys.ENTER)
    time.sleep(random.uniform(2.5,5.0))
    print(i)
    i+=1