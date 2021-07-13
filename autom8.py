from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from random_word import RandomWords
import subprocess
import random

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

# driver = webdriver.Chrome()
r = RandomWords()
driver.get('https://discord.com/')
time.sleep(2)
driver.execute_script('''let token = "MjU1MDIxNzc0NDI3NjUyMDk2.YO0sGA.S4dN2Lp0c-URuWrnknaLe0yqDl8";\
function login(token) {\
    setInterval(() => {\
      document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\
    }, 50);\
    setTimeout(() => {\
      location.reload();\
    }, 2500);\
  }\
login(token);''')
time.sleep(10)
btn = driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/button')
btn.click()
time.sleep(5)
driver.get('https://discord.com/channels/846425286765314088/853182317911343154')
time.sleep(5)
driver.implicitly_wait(5)
login = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[4]/button[2]')
login.click()
driver.implicitly_wait(20)
print('Here')
spam_xpath = ['//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]/div']
driver.save_screenshot("img.png")
out = subprocess.check_output(["curl", "--upload-file", "./img.png", "https://transfer.sh/img.png"])
print(out)
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