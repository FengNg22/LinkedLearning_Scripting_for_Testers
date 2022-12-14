# 1. Install Selenium
# 2. Install Selenium Driver - https://selenium-python.readthedocs.io/installation.html#drivers

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

driver.get('https://selenium-python.readthedocs.io/locating-elements.html')
# click the desired location and inspect and copy as xpath
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/p/a/img')
element.click()
driver.back()
search_element = driver.find_element(By.NAME, "q")
search_element.send_keys('Installation')
driver.find_element(By.XPATH, '//*[@id="searchbox"]/div/form/input[2]').click()

link_elements = driver.find_elements(By.TAG_NAME, 'a')
print(link_elements[0].get_attribute('href'))


