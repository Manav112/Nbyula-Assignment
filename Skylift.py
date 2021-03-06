import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.get('https://nbl.one/gigs/listings/careers1/chitkara-university-campus-hiring-software-test-engineer-internship-1')
driver.maximize_window()

time.sleep(3)
driver.find_element(By.XPATH, """//button[@id="skylift-book-seat"]""").click()
time.sleep(3)
driver.find_element(By.XPATH, """//button[@id="login-modal-continue-with-email"]""").click()
time.sleep(3)
driver.find_element(By.XPATH, """//input[@type='email']""").send_keys("email")
driver.find_element(By.XPATH, """//button[@id="login-custom"]""").click()
time.sleep(3)
driver.find_element(By.XPATH, """//input[@type='password']""").send_keys("password")
driver.find_element(By.XPATH, """//button[@id="login-custom"]""").click()
time.sleep(7)
driver.find_element(By.XPATH, """//span[text()="Proceed"]""").click()
time.sleep(3)
driver.find_element(By.XPATH, """//p[text()="Choose Billing Country"]""").click()
time.sleep(2)
driver.find_element(By.XPATH, """//button[text()="India"]""").click()
time.sleep(2)
driver.find_element(By.XPATH, """//p[text()="Choose Billing State"]""").click()
time.sleep(2)
driver.find_element(By.XPATH, """//button[text()="Himachal Pradesh"]""").click()
time.sleep(2)
driver.find_element(By.XPATH, """//button[@id="continue-to-pay-zero-dollar"]""").click()
time.sleep(2)
driver.quit()
