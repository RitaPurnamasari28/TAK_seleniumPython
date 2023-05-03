import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject.checkout_locator import checkout
from data.checkout_data import inputan
import login
from selenium.webdriver.support.ui import Select

class Checkout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

# untuk unitest pada awal nama case harus menggunakan test

    def test_success_checkout_demowebshop(self):
        driver = self.driver
        login.demowebshoplogin.test_success_login_demowebshop(self) #namafile-class-namacase
        # add to cart
        driver.find_element(By.XPATH, checkout.books_category).click()
        driver.find_element(By.XPATH, checkout.fictionbook).click()
        driver.find_element(By.ID, checkout.addtocart_btn).click()
        # Success Add to cart
        driver.find_element(By.ID, checkout.product_success_addt0_shopping_cart_msg)
        # Shopping cart
        driver.find_element(By.CLASS_NAME, checkout.shoppingcart).click()
        Select(driver.find_element(By.ID, checkout.country )).select_by_value(checkout.choosecountry)
        driver.find_element(By.ID, checkout.termofservice_checkbox).click()
        driver.find_element(By.ID, checkout.checkout_btn).click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/onepagecheckout")


    def test_failed_checkout_demowebshop_notcheck_termofservice(self):
        driver = self.driver
        login.demowebshoplogin.test_success_login_demowebshop(self) #namafile-class-namacase
        # add to cart
        driver.find_element(By.XPATH, checkout.books_category).click()
        driver.find_element(By.XPATH, checkout.fictionbook).click()
        driver.find_element(By.ID, checkout.addtocart_btn).click()
        # Shopping cart
        driver.find_element(By.CLASS_NAME, checkout.shoppingcart).click()
        driver.find_element(By.ID, checkout.checkout_btn).click()
        data = driver.find_element(By.ID, checkout.notcheck_termofservice_checkbox_msg).text
        self.assertIn(inputan.msg_notcheck_termofservice_checkbox, data)


    


def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

    #tekan arah atas untuk cari command di terminal