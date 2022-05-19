import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://omayo.blogspot.com/")
#driver.maximize_window()
driver.implicitly_wait(6)
driver.find_element(By.ID,"b-query").send_keys("hi")
driver.find_element(By.ID,"b-query-icon").click()
driver.find_element(By.ID,"home").click()
time.sleep(3)
driver.find_element(By)
