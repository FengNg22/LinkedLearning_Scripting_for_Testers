from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

driver.get('https://www.signaturemarket.co/my/marketplace/snack/all/3/12/New_Products.html')

# parent = driver.current_window_handle
# time.sleep(10)
# uselessWindows = driver.window_handles
# for winId in uselessWindows:
#     if winId != parent:
#         driver.switch_to.window(winId)
#         driver.close()

products = driver.find_elements(By.CLASS_NAME, "weight-title")

for index, product in enumerate(products):
    # hover = ActionChains(driver).move_to_element(card_price)
    # hover.perform()
    print(index)
    print(product)
    product = driver.find_element(By.XPATH, '/html/body/div[5]/div[5]/ul/li[%s]/div[2]/div[6]/div[1]' % int(index+1))
    product.click()

# search_elements = driver.find_elements(By.XPATH, "//span[@class='PropertyCardPrice__Value']")
# time.sleep(1)
#
# price_list = []
#
# for price in search_elements:
#     price_list.append(price.text)
#
# print(sorted(price_list))
