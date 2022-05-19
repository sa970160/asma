from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("hello world")
driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
time.sleep(3)
driver.find_element(By.ID, "//*[@id=").is_selected()
driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[6]/a").click()
time.sleep(3)
