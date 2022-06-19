import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')

driver.get('https://nbl.one')
driver.maximize_window()

Search_bar = driver.find_element_by_id('global-search-bar')
Search_bar.click()
Search_bar.send_keys('Recmas')
time.sleep(5)
driver.quit()