

from selenium import webdriver
import time, os, sys, json


def selectVersionCategory(category):

    if 'Current and Supported' == category:
        return 1
    elif category == None:
        return None
    elif 'Non Supported' == category:
        return 2
    elif 'Upcoming not Supported' == category:
        return 3

baseurl  ='https://swim-registry-brazil.herokuapp.com/en/'

driver  = webdriver.Chrome('/usr/local/share/chromedriver')

driver.get(baseurl+'login/')

username = driver.find_element_by_id("id_username")
password = driver.find_element_by_id("id_password")

username.send_keys("user@user.user")
password.send_keys("user12345")



driver.find_element_by_xpath('/html/body/div/form/button').click()

driver.get(baseurl+'services/new')


with open('eurServices.json', 'rb') as js:
    data = json.load(js)

print type(data)

#print data
for services in data:

        driver.find_element_by_id('name_id').send_keys(data[services]['header']['nameService'])

        driver.find_element_by_id('description_id').send_keys(data[services]['registrationProcess']['serviceDescription'])

        driver.find_element_by_id('version_id').send_keys(data[services]['header']['version'])

        driver.find_element_by_id('').send_keys(data[services]['versionCategory'])

        driver.find_element_by_id('').send_keys(data[services])

        driver.find_element_by_id('').send_keys(data[services])

        driver.find_element_by_id('').send_keys(data[services])

        driver.find_element_by_id('').send_keys(data[services])

        break

time.sleep(15)

driver.close()
