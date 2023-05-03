import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageobject.login_locator import login
from data.login_data import inputan
from data.baseurl import baseurl

class demowebshoplogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login_demowebshop(self):
        driver = self.driver
        driver.get(baseurl.baseURL)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, login.login_menu).click()
        driver.find_element(By.ID, login.email).send_keys(inputan.email)
        driver.find_element(By.ID, login.passworrd).send_keys(inputan.password)
        driver.find_element(By.XPATH, login.login_btn).click()
        data = driver.find_element(By.CLASS_NAME, login.loginsuccess).text
        self.assertIn(inputan.login_success, data)

    def test_failed_login_demowebshop_wrong_password(self):
        driver = self.driver
        driver.get(baseurl.baseURL)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, login.login_menu).click()
        driver.find_element(By.ID, login.email).send_keys(inputan.email)
        driver.find_element(By.ID, login.passworrd).send_keys(inputan.wrongpassword)
        driver.find_element(By.XPATH, login.login_btn).click()
        data = driver.find_element(By.CLASS_NAME, login.loginfailed).text
        self.assertIn(inputan.login_password_incorrect, data)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

    #tekan arah atas untuk cari command di terminal