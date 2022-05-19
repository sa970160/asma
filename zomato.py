import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdrivermanager import ChromeDriverManager


class TestUntitled():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(r"C:\Users\SALEEM_\Desktop\chrome driver\chromedriver.exe")
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get("https://www.flipkart.com/")
        self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a").click()

        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/form/div[1]/input").send_keys("9701604746")
        self.driver.find_element(By.NAME,"password").send_keys("6281861488")
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/form/div[4]/button/span").click()





