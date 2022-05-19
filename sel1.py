
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.find_element(By.ID,"RESULT_TextField-1").send_keys("salim")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("syed")
driver.find_element(By.ID,"RESULT_TextField-3").send_keys("9701604746")
driver.find_element(By.ID,"RESULT_TextField-4").send_keys("india")
driver.find_element(By.ID,"RESULT_TextField-5").send_keys("hyd")
driver.find_element(By.ID,"RESULT_TextField-6").send_keys("ssmalik26jan@gmail.com")
time.sleep(3)
#radio buttons:
status=driver.find_element(By.XPATH,"//*[@id='q26']/table/tbody/tr[1]/td/label").is_selected()
driver.find_element(By.XPATH,"//*[@id='q26']/table/tbody/tr[1]/td/label").click()
time.sleep(2)
#check boxes:
driver.find_element(By.XPATH,"//*[@id='q15']/table/tbody/tr[2]/td/label").click()
driver.find_element(By.XPATH,"//*[@id='q15']/table/tbody/tr[6]/td/label").click()
time.sleep(3)
#drop downs:
drp = Select(driver.find_element(By.ID,"RESULT_RadioButton-9"))
drp.select_by_value("Radio-2")
time.sleep(3)






