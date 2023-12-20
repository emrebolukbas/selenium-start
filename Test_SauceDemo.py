from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Test_SauceDemo:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() #ekranı büyütür
        sleep(1)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(1)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(1)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu: {testResult}")

testClass = Test_SauceDemo()
testClass.test_invalid_login()