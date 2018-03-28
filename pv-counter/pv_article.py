# coding: shift_jis
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

for i in range(10):
  options = Options()
  options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
  driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\chromedriver\\chromedriver.exe")
  driver.get("https://www.google.co.jp/")
  driver.find_element_by_id("lst-ib").send_keys("ヘイローアイ 海外セレブ")
  driver.find_element_by_name("btnK").click()
  driver.find_element_by_css_selector("#rso > div:nth-child(2) > div > div:nth-child(1) > div > div > h3 > a").click()
  sleep(3)
  driver.close()
  sleep(5)
