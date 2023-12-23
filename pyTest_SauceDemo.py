from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
import pytest


"""Bir önceki ödevde yazdığınız tüm testleri PyTest uyumlu hale getiriniz.
Kullandığımız SauceDemo sitesinde kendi belirlediğiniz en az "3" test case daha yazınız.
En az 1 testiniz parametrize fonksiyonu ile en az 3 farklı veriyle test edilmelidir. """

#1. case = ürün sepete ekleniyor mu?
#2. case = sepete doğru ürünler gidiyor mu ?
#3. case = alışverişi tamamla

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
        
class sauceDemoProducts:
    #1. case = ürün sepete ekleniyor mu?
    def added_Products(self):
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
        addToCart1 = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addToCart1.click()
        sleep(2)
        cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
        if (cart.text == "1"):
            pass
        else:
            print("product not added")
        addToCart2 = driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        addToCart2.click()
        sleep(2)
        testResult = cart.text == "2"
        print (f"Test Sonucu = {testResult}")
        
    #2. case = sepete doğru ürünler gidiyor mu ?
    def areCorrect_Products(self):
        
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
        addToCart1 = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addToCart1.click()
        sleep(2)
        addToCart2 = driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        addToCart2.click()
        sleep(2)
        firstProduct = driver.find_element(By.XPATH,"//*[@id='item_4_title_link']/div").text
        secondProduct = driver.find_element(By.XPATH,"//*[@id='item_0_title_link']/div").text
        cart = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        cart.click()
        sleep(2)
        product_control_1 = driver.find_element(By.XPATH,"//*[@id='item_4_title_link']/div").text
        product_control_2 = driver.find_element(By.XPATH,"//*[@id='item_0_title_link']/div").text
        sleep(2)
        testResult = (firstProduct and product_control_1 == "Sauce Labs Backpack") and (secondProduct and product_control_2 == "Sauce Labs Bike Light")
        print (f"Test Sonucu = {testResult}")
        
    #3. case = alışverişi tamamla
    def completeShopping(self):
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
        addToCart1 = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addToCart1.click()
        sleep(2)
        addToCart2 = driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        addToCart2.click()
        sleep(2)
        goCart = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        goCart.click()
        sleep(2)
        Checkout = driver.find_element(By.ID,"checkout")
        Checkout.click()
        sleep(2)
        fistName = driver.find_element(By.ID,"first-name")
        fistName.send_keys("Emre")
        sleep(2)
        lastName = driver.find_element(By.ID,"last-name")
        lastName.send_keys("Bolukbas")
        sleep(2)
        postalCode = driver.find_element(By.ID,"postal-code")
        postalCode.send_keys("12345")
        sleep(2)
        Continue = driver.find_element(By.ID,"continue")
        Continue.click()
        sleep(2)
        current_url = driver.current_url
        expected_url = "https://www.saucedemo.com/checkout-step-two.html"
        if ( expected_url == current_url):
            secondTest = True
        else:
            secondTest = False
        finishShopping = driver.find_element(By.ID,"finish")
        finishShopping.click()
        sleep(2)
        completeHeader = driver.find_element(By.CLASS_NAME,"complete-header")
        TestResult = completeHeader.text == "Thank you for your order!"
        print (f"Test Sonucu ={TestResult}")
        sleep(2)

        


         
"""          
testLogin = sauceDemoLogin()
testLogin.username_password_empty()
testLogin.password_empty_pass()
testLogin.invalid_login()
testLogin.product_control() """

testProducts = sauceDemoProducts()
testProducts.added_Products()
testProducts.areCorrect_Products()
testProducts.completeShopping()