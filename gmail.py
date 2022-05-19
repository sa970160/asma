import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.vn2solutions.com:2096/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='user']").send_keys('syed.salim@vn2solutions.com')
time.sleep(2)
driver.find_element(By.ID,"pass").send_keys("Salim@1234")
time.sleep(2)
login = driver.find_element(By.NAME,'login')
login.submit()
time.sleep(3)
driver.find_element(By.ID,"activeClientLogo").click()
time.sleep(3)
driver.find_element(By.ID,"rcmbtn104").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='compose_to']/div/div/ul/li/input").send_keys("gowthamkaza@gmail.com")
time.sleep(3)
driver.find_element(By.ID,"compose-subject").send_keys("Hi")
time.sleep(3)
driver.find_element(By.ID,"composebody").send_keys("Hi goutham how r u")
time.sleep(3)
driver.find_element(By.ID,"rcmbtn113").click()
time.sleep(5)



