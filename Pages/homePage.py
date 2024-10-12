from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    burgemenu = "react-burger-menu-btn"
    addBackPack_id = "add-to-cart-sauce-labs-backpack"
    removeButton_id = "remove-sauce-labs-backpack"
    cart_xpath = "//span[@class='shopping_cart_badge'][contains(.,'1')]"

    def __init__(self, driver):
        self.driver = driver

    def verifyBurgerMenu(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.burgemenu)))
        element.is_displayed()

    def selectBAckPack(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.addBackPack_id)))
        element.click()

    def verifyRemoveIdDisplayed(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.removeButton_id))).text

        if element=='Remove':
            assert True
        else:
            assert False

    def clickCart(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.cart_xpath)))
        element.click()




