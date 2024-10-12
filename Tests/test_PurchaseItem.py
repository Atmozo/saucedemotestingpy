import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver

from Pages.CheckoutPage import CheckoutPage
from Pages.cartPage import CartPage
from Pages.checkoutOverviewPage import CheckoutOverviewPage
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Utils.readProperties import ReadConfig


class Test_001_Login:
    sauceDemoURL = ReadConfig().getSauceDemoURL()
    username = ReadConfig().getUsername()
    password = ReadConfig().getPasswo2rd()
    firstName = ReadConfig().getFirstName()
    lastName = ReadConfig().getLastName()
    ZipCode = ReadConfig().getZipCode()

    @pytest.mark.regression
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginTests(self, setup: WebDriver | WebDriver | WebDriver):
        self.driver = setup
        self.driver.get(self.sauceDemoURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.cp = CartPage(self.driver)
        self.ck = CheckoutPage(self.driver)
        self.checkOutOverView = CheckoutOverviewPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login page", attachment_type=AttachmentType.PNG)
        self.lp.clickLogin()
        self.hp.verifyBurgerMenu()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
        self.hp.selectBAckPack()
        allure.attach(self.driver.get_screenshot_as_png(), name="item added to cart",
                      attachment_type=AttachmentType.PNG)
        self.hp.verifyRemoveIdDisplayed()
        self.hp.clickCart()
        allure.attach(self.driver.get_screenshot_as_png(), name="cart page screen",
                      attachment_type=AttachmentType.PNG)
        self.cp.verifyYourCartTitleIsDisplayed()
        self.cp.clickCheckoutButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="checkout screen",
                      attachment_type=AttachmentType.PNG)
        self.ck.setFirstName(self.firstName)
        self.ck.setLastName(self.lastName)
        self.ck.setPostalCode(self.ZipCode)
        allure.attach(self.driver.get_screenshot_as_png(), name="User Information Screen",
                      attachment_type=AttachmentType.PNG)
        self.ck.clickContinueButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="checkout overview screen",
                      attachment_type=AttachmentType.PNG)

        #Calculate cart total#
        self.checkOutOverView.verify_on_product_overview_page()
        self.checkOutOverView.calculate_cart_items()
        self.checkOutOverView.click_finish_btn()



        self.driver.quit()