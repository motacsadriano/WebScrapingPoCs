from selenium import webdriver
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from fake_useragent import UserAgent

ua = UserAgent()
userAgent = ua.random
print(userAgent)

options = webdriver.ChromeOptions() 
#options.add_argument('headless')
options.add_argument("--user-agent=New User Agent")
#url = 'https://www.webmotors.com.br/carros-novos/estoque/chevrolet?tipoveiculo=carros-novos&marca1=CHEVROLET'
#url = 'https://www.webmotors.com.br/carros-novos/estoque/fiat?tipoveiculo=carros-novos&marca1=FIAT'
url = 'https://www.webmotors.com.br/carros-novos/estoque/volkswagen?tipoveiculo=carros-novos&marca1=VOLKSWAGEN'
#url = 'https://www.webmotors.com.br/carros-novos/estoque/volkswagen?tipoveiculo=carros-novos&marca1=FORD'
#url = 'https://www.webmotors.com.br/carros-novos/estoque/toyota?tipoveiculo=carros-novos&marca1=TOYOTA'

#Importing Google Chrome Driver
driver = webdriver.Chrome('C:/chromedriver',options=options)

#Opening Browser with URL
driver.get(url)

SCROLL_PAUSE_TIME = 3
# Get scroll height 
last_height = driver.execute_script("return document.body.scrollHeight")

while True: 
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page 
    sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    sleep(SCROLL_PAUSE_TIME)

sleep(5)
#Getting content of the Scrapped Page and Parsing
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")

#Creating Array of Info
carNames=[]
carDescs=[]
carPrices=[]

#Looping the DIVs with the Vehicles to be scrapped
for car in soup.findAll('div',attrs={'class':'sc-kpOJdX dYHWQi'}):
    carName = car.find("h2",{"class":"sc-chPdSV blqZkq"})
    carDesc = car.find("h3",{"class":"sc-kgoBCf hSyDUf"})
    carPrice = car.find("strong",{"class":"sc-jTzLTM dAKzyv"})
    carNames.append(carName.text)
    carDescs.append(carDesc.text)
    carPrices.append(carPrice.text)

#Saving inormation into a CSV file
df = pd.DataFrame({'CAR NAME':carNames,'PRICE':carPrices,'DESC':carDescs}) 
df.to_csv('wemotors_vw.csv', index=False, encoding='utf-8')

#Closing the Browser
driver.quit()