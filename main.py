from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com")
sleep(3)
input = driver.find_element(By.NAME,"q")
input.send_keys("kodlama.io")
sleep(3)
searchButton = driver.find_element(By.NAME,"btnK")
searchButton.click()
sleep(3)
firstResult = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
firstResult.click()
sleep(3)
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
testResult = len(listOfCourses) == 7
print(f"Test Sonucu : {testResult}")