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
        self.driver = webdriver.Chrome(r"C:\Users\SALEEM_\Downloads\Chrome Driver\chromedriver.exe")
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get("https://www.vn2solutions.com:2096")
        self.driver.find_element(By.ID, "user").send_keys("syed.salim@vn2solutions.com")

        self.driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys("Salim@1234")

        self.driver.find_element(By.ID, 'login_submit').click()
        time.sleep(5)
        self.driver.find_element(By.ID, "activeClientLogo").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "rcmbtn104").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='compose_to']/div/div/ul/li/input").send_keys(
            "gowtham.kaza@vn2solutions.com")
        time.sleep(5)
        self.driver.find_element(By.ID, "compose-subject").send_keys("hi")
        time.sleep(5)
        self.driver.find_element(By.ID, "composebody").send_keys("Hi gowtham how r u")
        time.sleep(5)
        self.driver.find_element(By.ID, "rcmbtn113").click()
        time.sleep(10)
