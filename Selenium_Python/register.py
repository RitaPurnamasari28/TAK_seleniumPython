import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageobject.register_locator import register
from data.register_data import inputan
from data.baseurl import baseurl

class demowebshopregister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

# untuk unitest pada awal nama case harus menggunakan test

    def test_success_register_demowebshop(self):
        driver = self.driver
        driver.get(baseurl.baseURL)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,register.register_menu).click()
        driver.find_element(By.ID, register.genderfemale).click()
        driver.find_element(By.ID, register.firstname).send_keys(inputan.firstname)
        driver.find_element(By.ID, register.lastname).send_keys(inputan.lastname)
        driver.find_element(By.ID, register.email).send_keys(inputan.email_register_success) #jangan lupa ganti email setelah run
        driver.find_element(By.ID, register.passworrd).send_keys(inputan.password)
        driver.find_element(By.ID, register.confirmpassword).send_keys(inputan.password)
        driver.find_element(By.ID, register.register_btn).click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/registerresult/1")
        data = driver.find_element(By.CLASS_NAME, register.registersuccess).text
        self.assertIn(inputan.register_success_msg, data)

    def test_failed_register_demowebshop_not_submit_passwords(self):
        driver = self.driver
        driver.get(baseurl.baseURL)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, register.register_menu).click()
        driver.find_element(By.ID, register.genderfemale).click()
        driver.find_element(By.ID, register.firstname).send_keys(inputan.firstname)
        driver.find_element(By.ID, register.lastname).send_keys(inputan.lastname)
        driver.find_element(By.ID, register.email).send_keys(inputan.email_register_failed)
        driver.find_element(By.ID, register.register_btn).click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register") # validasi bahwa tidak redirect krna failed setelah tap button register
        data = driver.find_element(By.CLASS_NAME, register.registerfailed).text
        self.assertIn(inputan.register_failed_msg, data)

def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

    #tekan arah atas untuk cari command di terminal