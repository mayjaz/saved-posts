from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import urllib.request
import os
import requests
import wget

#options = webdriver.ChromeOptions()
#options.add_argument("headless")
driver = webdriver.Chrome('C:\\Users\\User\\Desktop\\driver\\chromedriver.exe') #driver path
driver.get("https://www.instagram.com/")

user = input('enter your username: ')
pwd = input('enter your password: ')

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys(user)
password.send_keys(pwd)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

driver.get("https://www.instagram.com/" + user + "/saved")
driver.execute_script("window.scrollTo(0,4000);")
sleep(10)
images = driver.find_elements_by_tag_name('img')
sleep(5)
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path, "IG saved posts")

os.mkdir(path)
keyword = input('save images as: ')
counter = 0
for image in images:
    save_as = os.path.join(path, keyword + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

driver.quit()

