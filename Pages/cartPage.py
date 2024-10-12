from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    title_YourCart_xpath = "//span[@class='title'][contains(.,'Your Cart')]"
    checkoutButton_id = "checkout"
    def __init__(self, driver):
        self.driver = driver

    def verifyYourCartTitleIsDisplayed(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.title_YourCart_xpath)))
        element.is_displayed()

    def clickCheckoutButton(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.checkoutButton_id)))
        element.click()

