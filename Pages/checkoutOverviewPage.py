from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutOverviewPage:

    overviewPageTitle = "//span[@class='title'][contains(.,'Checkout: Overview')]"
    cartList = "cart_list"
    cartItem = "cart_item"
    subTotalLbl = "//div[contains(@class,'summary_subtotal_label')]"
    taxLbl = "//div[contains(@class,'summary_tax_label')]"
    totalLbl = "//div[contains(@class,'summary_total_label')]"
    finishBtn = "finish"

    def __init__(self, driver):
        self.driver = driver

    def verify_on_product_overview_page(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.overviewPageTitle)))

    def calculate_cart_items(self):
        cart = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, self.cartList)))
        items = cart.find_elements(By.CLASS_NAME, self.cartItem)
        if items.__len__() > 0:
            item_sub_total = float(cart.find_element(By.XPATH, self.subTotalLbl).text.split(" ")[2].split("$")[1])
            item_total = float(cart.find_element(By.XPATH, self.totalLbl).text.split(" ")[1].split("$")[1])
            tax_percent = 0.08
            tax_amount = item_sub_total * tax_percent
            temp_total = item_sub_total + tax_amount
            if float(temp_total.__format__(".2f")) == item_total:
                assert True
            else:
                assert False

    def click_finish_btn(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, self.finishBtn))).click()