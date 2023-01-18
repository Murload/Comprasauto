import unittest
from os import remove
from selenium import webdriver
from time import sleep
import random  
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Funcionesglobales.funciselenium import Funciones_Globales
from Funcionesglobales.roleapplicant import Applicant


pricecot = random.randint(100000, 999999)
companyran = random.randint(1, 99)
iva = random.randint(1, 5)
methodpay = random.randint(1, 4)

class Analyst(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def managerequestAnaAccept(self):
        f = Funciones_Globales(self.driver)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 1)
        f.Click_Mixto("xpath", "(//span[@class='mat-button-wrapper'][contains(.,'Gestionar')])[1]", 1)
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 3)  
        f.Click_NotScroll("(//span[@class='mat-option-text'])[1]")
        f.Click_Mixto("xpath", "(//div[contains(.,'Cotización 1')])[9]", 2)
        f.Click_NotScroll('/html/body/div[2]/div[2]/div/mat-dialog-container/app-procesar-solicitud/div/form/mat-dialog-content/div[8]/div[2]/div[1]/mat-form-field/div/div[1]/div[2]/i')
        # f.uploadfile("C:\\Users\\Montechelo\\Desktop\\Comprasauto\\filesupload\\cotizacion1.pdf")
        f.uploadfile("C:\\Users\\aleon\\Desktop\\Comprasauto\\filesupload\\cotizacion1.pdf")
        sleep(2)
        f.Texto_Mixto("xpath", "(//input[@aria-required='true'])[2]", pricecot ,1)
        sleep(2)
        f.Texto_Mixto("xpath", "(//input[@type='text'])[5]", "Observación cotizaciones automaticas." ,1)
        sleep(2)
        f.Click_NotScroll("(//button[contains(@type,'button')])[6]")
        sleep(1)
        f.Click_NotScroll("(//button[@type='button'])[9]")
        sleep(6)


    def managerequestAnaback(self):
        f = Funciones_Globales(self.driver)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 1)
        f.Click_Mixto("xpath", "(//span[@class='mat-button-wrapper'][contains(.,'Gestionar')])[2]", 1)
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 3)  
        f.Click_NotScroll("(//span[@class='mat-option-text'])[2]")
        f.Texto_Mixto("xpath", "(//input[@type='text'])[2]", "Observación devuelta automaticamente", 2)
        sleep(2)
        f.Click_NotScroll("(//button[@color='primary'])[4]")
        sleep(1)
        f.Click_NotScroll("(//button[@type='button'])[8]")
        sleep(4)

    def order(self):
        f = Funciones_Globales(self.driver)
        roleapplicant = Applicant(self.driver)
        # product = roleapplicant.createnewrequest()
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 1)
        sleep(3)
        f.Click_Mixto("xpath", "(//span[contains(.,'Orden')])[1]", 2)
        f.Textkeyenenter("(//input[@aria-invalid='false'])[2]")
        sleep(1)
        f.Click_NotScroll("//button[contains(.,'Generar Orden')]")
        sleep(4)
        # f.Texto_Mixto("xpath", "(//input[@aria-invalid='false'])[2]", "793478952", 3)
        f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 2)
        sleep(4)
        textdetails= self.driver.find_element(By.XPATH, "(//input[contains(@type,'text')])[1]")
        textdetails.send_keys("Producto", Keys.TAB ,"Especificación", Keys.TAB, companyran, Keys.TAB,
        pricecot)
        f.Click_NotScroll("(//div[contains(.,'IVA')])[12]")
        f.Click_NotScroll("(//span[@class='mat-option-text'])[{}]".format(iva))
        sleep(3)
        f.Click_Mixto("xpath", "(//button[@color='primary'][contains(.,'Siguiente')])[2]", 2)
        sleep(3)
        f = Funciones_Globales(self.driver)
        f.Texto_Mixto("xpath", "(//input[@type='text'])[3]", "Observación de Orden de compra automatica.",2)
        f.Texto_Mixto("xpath", "(//input[@aria-required='true'])[6]", "0",2)
        sleep(3)
        f.Texto_Mixto("xpath", "//input[@type='date']", "20012023",2)
        f.Click_NotScroll("(//div[contains(.,'Método de pago')])[9]")
        f.Click_NotScroll("(//span[@class='mat-option-text'])[{}]".format(methodpay))
        sleep(3)
        f.Click_NotScroll("(//div[contains(.,'Condición de pago')])[9]")
        valueabo = self.driver.find_element(By.XPATH, "(//span[contains(@class,'mat-option-text')])[1]")
        ActionChains(self.driver).click(valueabo).send_keys(Keys.TAB,"1000000", Keys.TAB,"5", Keys.TAB, Keys.ARROW_RIGHT,
        Keys.TAB, Keys.ARROW_RIGHT, Keys.TAB, "Ciudad auto", Keys.TAB,"Direccion auto", Keys.TAB,"Observaciones de condiciones auto").perform() 
        sleep(5)
        f.Click_Mixto("xpath", "(//button[@type='button'])[10]", 5)
        

    
        

        



        


        