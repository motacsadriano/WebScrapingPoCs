from selenium import webdriver
import pandas as pd
from time import sleep

#Importing Google Chrome Driver
driver = webdriver.Chrome('C:/chromedriver')

#Opening Browser with URL
driver.get("https://www.renault.com.br/")

sleep(2)
#In this case, we're going to get the Kwid Page. Geting the Xpath of the Link for this car and clicking on it
driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[5]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/a[1]/span').click()

#Creating Arrays to append information for upcoming CSV File
carNames =[]
carModels = []
carPrices = []

#Getting the Car Name and printing it on the Console
kwidName = driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[12]/div/div[1]/div[1]/div/div/div/div/h2/span').text

#Getting all the Models from Kwid
models = driver.find_elements_by_class_name('car-title')
for carModel in models:
    carModels.append(carModel.text)
    carNames.append(kwidName)

#Getting all the Prices from Kwid
prices = driver.find_elements_by_class_name('full-price')
for carPrice in prices:
    carPrices.append(carPrice.text)

sleep(2)
#Getting the Xpath for the Home Logo Button. After finding it, clicking to go home
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/header/div/div[2]/div[1]/span/a').click()

sleep(2)
#In this case, we're going to get the Duster Page. Geting the Xpath of the Link for this car and clicking on it
driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[5]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/a[4]/span').click()

sleep(2)
#Getting the Car Name and printing it on the Console
dusterName = driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[5]/div/div[1]/div[1]/div/div/div/div/h2/span').text

#Getting all the Models from Duster
models = driver.find_elements_by_class_name('car-title')
for carModel in models:
    carModels.append(carModel.text)
    carNames.append(dusterName)

#Getting all the Prices from Duster
prices = driver.find_elements_by_class_name('full-price')
for carPrice in prices:
    carPrices.append(carPrice.text)

sleep(2)
#Getting the Xpath for the Home Logo Button. After finding it, clicking to go home
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/header/div/div[2]/div[1]/span/a').click()

sleep(2)
#In this case, we're going to get the Captur Page. Geting the Xpath of the Link for this car and clicking on it
driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[5]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/a[2]/span').click()

sleep(2)
#Getting the Car Name and printing it on the Console
capturName = driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[6]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div/h2/span').text

#Getting all the Models from Captur
models = driver.find_elements_by_class_name('car-title')
for carModel in models:
    carModels.append(carModel.text)
    carNames.append(capturName)

#Getting all the Prices from Sandero
prices = driver.find_elements_by_class_name('full-price')
for carPrice in prices:
    carPrices.append(carPrice.text)

#Generating an CSV File with all the information we scrapped =)
df = pd.DataFrame({'Product Name':carNames,'Models':carModels,'Prices':carPrices}) 
df.to_csv('renault.csv', index=False, encoding='utf-8')

#Closing the Browser
driver.quit()