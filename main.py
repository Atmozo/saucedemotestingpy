import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

product = driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text

if product == 'Products':
    print('Login was successful')
    assert True
else:
    print('Login was not successful')
    assert False
#driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(5)
# Close the browser
driver.quit()


#We use the below to run ALL Tests in the Terminal
# pytest -s -v -m"regression" --alluredir="allure-results" --browser chrome
