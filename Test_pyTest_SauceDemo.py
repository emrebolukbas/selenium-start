from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest


"""Bir önceki ödevde yazdığınız tüm testleri PyTest uyumlu hale getiriniz.
Kullandığımız SauceDemo sitesinde kendi belirlediğiniz en az "3" test case daha yazınız.
En az 1 testiniz parametrize fonksiyonu ile en az 3 farklı veriyle test edilmelidir. """

#pytest koşturabilmek için class isimlerine büyük T ile Test_ fonksiyonlara ise küçük t ile test_ isimlendirerek başla yoksa tanımlamaz !!!
class Test_sauceDemoLogin:
    def setup_method(self): #her test başlangıcında çalışacak fonk.
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() #ekranı büyütür

    def teardown_metahod(self): #her testin bitiminde çalışacak fonk.
        self.driver.quit()

    def test_username_password_empty(self):
         loginButtton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, 'login-button')))
         loginButtton.click()
         errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
         assert errorMessage.text == "Epic sadface: Username is required"

    def test_password_empty_pass(self):
        userName = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, "user-name")))
        userName.send_keys("standard_user")
        loginButtton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, 'login-button')))
        loginButtton.click()
        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        assert errorMessage.text == "Epic sadface: Password is required"
          
    def test_invalid_login(self):
        userName = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, "user-name")))
        userName.send_keys("locked_out_user")
        password = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, "password")))
        password.send_keys("secret_sauce")
        loginButtton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, 'login-button')))
        loginButtton.click()
        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."


    def test_product_control(self):
        userName = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        userName.send_keys("standard_user")
        password = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        password.send_keys("secret_sauce")
        loginButtton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, 'login-button')))
        loginButtton.click()
        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (expected_url == current_url ):
            firstTest = True
        else:
            firstTest = False
        products = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,'inventory_item_label')))
        secondTest = len(products) == 6
        assert firstTest == True and secondTest == True 

#1. case = ürün sepete ekleniyor mu?
#2. case = sepete doğru ürünler gidiyor mu ?
#3. case = alışverişi tamamla        
class Test_sauceDemoProducts:
     #prefix => test_
    def setup_method(self): #her test başlangıcında çalışacak fonk.
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() #ekranı büyütür

    def teardown_metahod(self): #her testin bitiminde çalışacak fonk.
        self.driver.quit()

    #1. case = ürün sepete ekleniyor mu?
    @pytest.mark.parametrize("username_param, password_param", [("standard_user", "secret_sauce"),("error_user","secret_sauce")])
    def test_added_Products(self,username_param,password_param):
        userName = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, "user-name")))
        userName.send_keys(username_param)
        password = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, "password")))
        password.send_keys(password_param)
        loginButtton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, 'login-button')))
        loginButtton.click()
        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (expected_url == current_url ):
            firstTest = True
        else:
            firstTest = False
        addToCart1 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart1.click()
        cart = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        if (cart.text == "1"):
            pass
        else:
            print("product not added")
        addToCart2 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-bike-light")))
        addToCart2.click()
        assert cart.text == "2"
    #2. case = sepete doğru ürünler gidiyor mu ?
    def test_areCorrect_Products(self):
        userName = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, "user-name")))
        userName.send_keys("standard_user")
        password = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, "password")))
        password.send_keys("secret_sauce")
        loginButtton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, 'login-button')))
        loginButtton.click()
        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (expected_url == current_url ):
            firstTest = True
        else:
            firstTest = False
        addToCart1 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart1.click()
        addToCart2 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-bike-light")))
        addToCart2.click()
        firstProduct = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='item_4_title_link']/div"))).text
        secondProduct = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='item_0_title_link']/div"))).text
        cart = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
        cart.click()
        product_control_1 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='item_4_title_link']/div"))).text
        product_control_2 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='item_0_title_link']/div"))).text
        assert (firstProduct and product_control_1 == "Sauce Labs Backpack") and (secondProduct and product_control_2 == "Sauce Labs Bike Light")
        
    #3. case = alışverişi tamamla
    def test_completeShopping(self):
        userName = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, "user-name")))
        userName.send_keys("standard_user")
        password = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, "password")))
        password.send_keys("secret_sauce")
        loginButtton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID, 'login-button')))
        loginButtton.click()
        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"
        if (expected_url == current_url ):
            firstTest = True
        else:
            firstTest = False
        addToCart1 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart1.click()
        addToCart2 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-bike-light")))
        addToCart2.click()
        goCart = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
        goCart.click()
        Checkout = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"checkout")))
        Checkout.click()
        fistName = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"first-name")))
        fistName.send_keys("Emre")
        lastName = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"last-name")))
        lastName.send_keys("Bolukbas")
        postalCode = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"postal-code")))
        postalCode.send_keys("12345")
        Continue = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"continue")))
        Continue.click()
        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/checkout-step-two.html"
        if ( expected_url == current_url):
            secondTest = True
        else:
            secondTest = False
        finishShopping = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.ID,"finish")))
        finishShopping.click()
        completeHeader = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CLASS_NAME,"complete-header"))).text
        assert completeHeader == "Thank you for your order!"


             
"""          
testLogin = sauceDemoLogin()
testLogin.username_password_empty()
testLogin.password_empty_pass()
testLogin.invalid_login()
testLogin.product_control() """

#testProducts = sauceDemoProducts()
#testProducts.added_Products()
#testProducts.areCorrect_Products()
#testProducts.completeShopping()