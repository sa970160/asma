import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("9701604746")
time.sleep(2)
driver.find_element(By.ID, "pass").send_keys('8008050605')
time.sleep(2)
login = driver.find_element(By.NAME, 'login')
login.submit()
time.sleep(10)


