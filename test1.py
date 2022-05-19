import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
driver.implicitly_wait(6)
driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
time.sleep(3)
driver.find_element(By.ID,"email_create").send_keys("ssmalik26jan@gmail.com")
driver.find_element(By.XPATH,"//*[@id='SubmitCreate']/span").submit()
time.sleep(5)
driver.find_element(By.ID,"id_gender1").click()
driver.find_element(By.ID,"customer_firstname").send_keys("salim")
driver.find_element(By.ID,"customer_lastname").send_keys("syed")
driver.find_element(By.ID,"passwd").send_keys("Sa@1234")
time.sleep(5)
driver.find_element(By.ID,"days").send_keys(26)
driver.find_element(By.ID,"months").send_keys("january")
driver.find_element(By.ID,"years").send_keys(1995)
time.sleep(3)
driver.find_element(By.ID,"newsletter").click()
driver.find_element(By.ID,"firstname").send_keys("salim")
driver.find_element(By.ID,"lastname").send_keys("syed")
driver.find_element(By.ID,"company").send_keys("ss enterprises")
driver.find_element(By.ID,"address1").send_keys("kundhanahalli")
driver.find_element(By.ID,"address2").send_keys("floor no-308")
driver.find_element(By.ID,"city").send_keys("banglore")
time.sleep(3)
drp = Select(driver.find_element(By.ID,"id_state"))
drp.select_by_visible_text("Indiana")
driver.find_element(By.ID,"postcode").send_keys("523333")
drp = Select(driver.find_element(By.ID,"id_country"))
drp.select_by_value("21")
driver.find_element(By.ID,"other").send_keys("siva pg, kundhanahalli,brookfeild.")
driver.find_element(By.ID,"phone").send_keys('8008050605')
driver.find_element(By.ID,"phone_mobile").send_keys('9701604746')
driver.find_element(By.ID,"alias").send_keys("boork feild")
driver.find_element(By.ID,"submitAccount").submit()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='block_top_menu']/ul/li[3]/a").click()



