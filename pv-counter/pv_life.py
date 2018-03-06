from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

while True:
  driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\chromedriver\\chromedriver.exe")
  driver.get("https://xxxxxxxxxxxxxx")
  driver.close()
  sleep(1)
