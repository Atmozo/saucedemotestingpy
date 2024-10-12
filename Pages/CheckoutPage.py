from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    textfistName_id = "first-name"
    textlastName_id = "last-name"
    textpostalCode_id = "postal-code"
    continueButton_id = "continue"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, firstName):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textfistName_id)))
        element.send_keys(firstName)

    def setLastName(self, lastName):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textlastName_id)))
        element.send_keys(lastName)

    def setPostalCode(self, ZipCode):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textpostalCode_id)))
        element.send_keys(ZipCode)

    def clickContinueButton(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.continueButton_id)))
        element.click()



