import time
from io import BytesIO
from PIL import Image
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import listdir
from os.path import abspath, dirname
from selenium import webdriver

url = 'https://www.zhihu.com/signin?next=http%3A%2F%2Fwww.zhihu.com%2F'
browser = webdriver.Chrome()

wait = WebDriverWait(browser, 20)
username = '13398681779'
password = '0476aaaa'


browser.delete_all_cookies()
browser.get(url)
username1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.SignFlow-accountInput input')))
password1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.SignFlow-password .Input-wrapper .Input')))
submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.SignFlow-submitButton')))
username1.send_keys(username)
password1.send_keys(password)
time.sleep(1)
submit.click()
time.sleep(20)
browser.quit()