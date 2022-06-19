import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.get('https://nbl.one/login')
driver.maximize_window()

driver.find_element(By.XPATH, """//input[@type='email']""").send_keys("test.hackerone08@gmail.com")
driver.find_element(By.XPATH, """//button[@id="login-custom"]""").click()
time.sleep(2)
driver.find_element(By.XPATH, """//input[@type='password']""").send_keys("1234567890")
driver.find_element(By.XPATH, """//button[@id="login-custom"]""").click()

