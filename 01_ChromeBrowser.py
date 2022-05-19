from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
# x = 10
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME, 'name').send_keys("Kiran Kumar")
time.sleep(2)
driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("ashgdhgf@"
                                                                  "gmail.com")
time.sleep(2)
driver.find_element(By.ID, 'exampleInputPassword1').send_keys("khdsgfdhgd")
time.sleep(2)
driver.find_element(By.XPATH, '//label[normalize-space()="Check me out if you Love IceCreams!"]').click()
time.sleep(2)
gender = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
gender.select_by_visible_text("Female")
time.sleep(2)
gender.select_by_index(0)
time.sleep(5)
employee_Ra = driver.find_element(By.ID, 'inlineRadio2').is_enabled()
print("status of emplyee_RD: ", employee_Ra)
if employee_Ra == True:
    driver.find_element(By.ID, 'inlineRadio2').click()
time.sleep(3)
status = driver.find_element(By.ID, 'inlineRadio3').is_enabled()
print("status of entrepreneus: ", status)
driver.find_element(By.XPATH, '//input[@value="Submit"]').click()
time.sleep(3)
#/html/body/app-root/form-comp/div/div/form/input
result = driver.find_element(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]').text
print("reustl is : ",result)
if "success" in result:
    print("Test case pass")
else:
    print("Test case failed")