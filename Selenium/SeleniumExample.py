# 1. Install Selenium
# 2. Install Selenium Driver - https://selenium-python.readthedocs.io/installation.html#drivers

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

driver.get('http://google.com')
# element = driver.find_element_by_name('q') # method has eliminated by Selenium
element = driver.find_element("name", "q")
element.send_keys('test')

from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.ENTER)


