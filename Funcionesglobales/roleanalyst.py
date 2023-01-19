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
        f.Click_Mixto("xpath", "(//span[contains(.,'Gestionar')])[1]", 1)
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 3)  
        f.Click_NotScroll("(//span[@class='mat-option-text'])[1]")
        f.Click_Mixto("xpath", "(//div[contains(.,'Cotización 1')])[9]", 2)
        f.Click_NotScroll('/html/body/div[2]/div[2]/div/mat-dialog-container/app-procesar-solicitud/div/form/mat-dialog-content/div[8]/div[2]/div[1]/mat-form-field/div/div[1]/div[2]/i')
        f.uploadfile("C:\\Users\\Montechelo\\Desktop\\Comprasauto\\filesupload\\cotizacion1.pdf")
        # f.uploadfile("C:\\Users\\aleon\\Desktop\\Comprasauto\\filesupload\\cotizacion1.pdf")
        sleep(2)
        f.Texto_Mixto("xpath", "(//input[@aria-required='true'])[2]", pricecot ,1)
        sleep(2)
        f.Texto_Mixto("xpath", "(//input[@type='text'])[5]", "Observación cotizaciones automaticas." ,1)
        sleep(2)
        f.Click_NotScroll("//button[contains(.,'Enviar')]")
        sleep(1)
        f.Click_NotScroll("//button[contains(.,'Aceptar')]")
        sleep(6)

    def managerequestAnaback(self):
        f = Funciones_Globales(self.driver)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 1)
        f.Click_Mixto("xpath", "(//span[contains(.,'Gestionar')])[1]", 1)
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 3)  
        f.Click_NotScroll("(//span[@class='mat-option-text'])[2]")
        f.Texto_Mixto("xpath", "(//input[@type='text'])[2]", "Observación devuelta automaticamente", 2)
        sleep(2)
        f.Click_NotScroll("//button[contains(.,'Enviar')]")
        sleep(1)
        f.Click_NotScroll("//button[contains(.,'Aceptar')]")
        sleep(4)

    def order(self):
        f = Funciones_Globales(self.driver)
        roleapplicant = Applicant(self.driver)
        # product = roleapplicant.createnewrequest()
        sleep(4)
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
        f.Click_Mixto("xpath", "(//button[@type='button'])[8]", 2)
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
        f.Click_Mixto("xpath", "(//button[@type='button'])[10]", 6)
        sleep(3)
        
    def sendorder(self):
        f = Funciones_Globales(self.driver)
        # f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 1)
        sleep(5)
        f.Click_NotScroll("(//div[contains(.,'Ordenes de compra')])[7]")
        f.Click_NotScroll("/html/body/app-root/app-mios/app-side-bar/div/mat-sidenav-container/mat-sidenav-content/div/app-solicitudes-list/div/mat-tab-group/div/mat-tab-body[2]/div/app-orden-compra-list/div[3]/table/tbody/tr[1]/td[1]/div/button[3]")
        f.Click_NotScroll("//button[contains(.,'Aceptar')]")
        sleep(10)


    def fragorder(self):
        f = Funciones_Globales(self.driver)
        companyrandiv = companyran % 2
        frag = companyran/2
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 1)
        f.Click_NotScroll("(//div[contains(.,'Ordenes de compra')])[7]")
        sleep(3)
        f.Click_NotScroll("(//i[@class='fi-rr-layout-fluid'])[1]")
        sleep(3)
        f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 2)
        if companyrandiv == 0:
            fragpar=(int(frag))
            asd = self.driver.find_element(By.XPATH, "(//input[contains(@type,'number')])[4]")
            print(asd.text)
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragpar, 5)
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]")
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 4)
            sleep(15)
            f.Click_NotScroll("(//i[@class='fi-rr-layout-fluid'])[1]")
            sleep(3)
            f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 2)
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragpar, 5)
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]")
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 4)
            sleep(10)
        else:
            fragimpar1 = (int(frag))
            fragimpar2 =(int(frag+1))
            asd = self.driver.find_element(By.XPATH, "(//input[contains(@type,'number')])[4]")
            print(asd.text)
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragimpar1, 5)
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]")
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 4)
            sleep(15)
            f.Click_NotScroll("(//i[@class='fi-rr-layout-fluid'])[1]")
            sleep(3)
            f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 2)
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragimpar2, 5)
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]")
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 4)
            sleep(10)



        

        



        


        