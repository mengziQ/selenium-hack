from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
import sys


while True:
  if datetime.now().strftime('%X')[:5] == "11:24":
    options = Options()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\02.drivers\\chrome_webdriver\\chromedriver.exe")

    # page 1
    driver.get("https://cl.i-abs.co.jp/e-clocking/login.asp")
    driver.switch_to.frame("f1")
    driver.find_element_by_name("DataSource").send_keys("xxxxx")
    driver.find_element_by_name("LoginID").send_keys("yyyyy")
    driver.find_element_by_name("PassWord").send_keys("zzzzz")
    driver.find_element_by_name("btnLogin").click()
  
    # page 2
    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.NAME, 'rbselect')))
    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.NAME, 'punch')))
    
    if sys.argv[1] == "--in":
      driver.execute_script("parent.f1.document.getElementsByName('rbselect').item(0).value = 1;")
    elif sys.argv[1] == "--out":
      driver.execute_script("parent.f1.document.getElementsByName('rbselect').item(0).value = 2;")
    else:
      print('please enter argument: "--in", "--out"')
    
    print('rbselect:', driver.find_element_by_name("rbselect").get_attribute("value"))
    print('punch:', driver.find_element_by_name("punch"))
    driver.find_element_by_name("punch").click()
  
    # page 3
    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.NAME, 'OK')))
    driver.find_element_by_name("OK").click()
  
    sys.exit()

