# coding: shift_jis
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

for i in range(10):
  options = Options()
  options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
  driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\chromedriver\\chromedriver.exe")
  driver.get("https://withonline.jp/")
  driver.find_elements_by_css_selector("html > body > div.header > div.container > div.search-icon > a > img")[0].click()
  driver.find_elements_by_css_selector("html > body > div.header > div.container > div.search-icon > form > div > input")[0].send_keys("ヘイローアイ")
  driver.execute_script("$('html > body > div.header > div.container > div.search-icon > form > div > button').click()")
  driver.find_elements_by_css_selector("html > body > div.content > div.row > div.col-sm-12 > div.content > div.row > div.col-sm-8 > div.list-group > div.article-4zlJ4 > a")[0].click()
  driver.close()
  sleep(10)
