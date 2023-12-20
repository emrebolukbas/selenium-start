from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#2- Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.
#Test Caseler;
#-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
#-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
#-Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
#-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

class sauceDemoLogin:
    
    def username_password_empty(self):
         driver = webdriver.Chrome()
         driver.get("https://www.saucedemo.com")
         sleep(2)
         loginButtton = driver.find_element(By.ID, 'login-button')
         loginButtton.click()
         sleep(5)
         errorMessage = driver.find_element(By.XPATH, "//h3[@data-test='error']")
         testResult = errorMessage.text == "Epic sadface: Username is required"
         print (f"1) Test Result : {testResult}")

    def password_empty_pass(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        userName = driver.find_element(By.ID, "user-name")
        userName.send_keys("standard_user")
        sleep(3)
        loginButtton = driver.find_element(By.ID, 'login-button')
        loginButtton.click()
        errorMessage = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        sleep(3)
        print (f"2) Test Result : {testResult}")
          
    def invalid_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        userName = driver.find_element(By.ID, "user-name")
        userName.send_keys("locked_out_user")
        sleep(3)
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        sleep(3)
        loginButtton = driver.find_element(By.ID, 'login-button')
        loginButtton.click()
        errorMessage = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        sleep(3)
        print (f"3) Test Result : {testResult}")     

    def product_control(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        userName = driver.find_element(By.ID, "user-name")
        userName.send_keys("standard_user")
        sleep(1)
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        sleep(1)
        loginButtton = driver.find_element(By.ID, 'login-button')
        loginButtton.click()
        sleep(2)
        current_url = driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (expected_url == current_url ):
            firstTest = True
        else:
            firstTest = False
        products = driver.find_elements(By.CLASS_NAME,'inventory_item_label')
        secondTest = len(products) == 6
        sleep(3)
        if (firstTest == True and secondTest == True):
            print ("4) Test Result : True")  
        else:
            print ("4) Test Result : False")  
        

         
         
testClass = sauceDemoLogin()
testClass.username_password_empty()
testClass.password_empty_pass()
testClass.invalid_login()
testClass.product_control()